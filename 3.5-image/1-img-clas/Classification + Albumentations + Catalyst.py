

#################################################################### IMPORT PACKAGES

import cv2
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
import albumentations as A
from albumentations.pytorch import ToTensorV2

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torchvision.transforms import Compose, Resize, ToPILImage, ToTensor

import catalyst
import catalyst.dl
import catalyst.data
from catalyst.contrib.nn.optimizers import Lamb, Lookahead, RAdam, QHAdamW
from catalyst.contrib.nn.criterion import (
    FocalLossMultiClass, HuberLoss, TripletLoss, IoULoss, MarginLoss # and many more
)

print("Pytorch: ", torch.__version__)
print("Catalyst:", catalyst.__version__)
print()


#################################################################### CONSTANTS

VALID_PCT  = 0.3
BATCH_SIZE = 32
EPOCHS     = 3
MAX_LR     = 1e-3
NUM_CLASES = 3

TRAIN_AUG = A.Compose([
    A.Resize(100, 100, always_apply=True),
    A.HorizontalFlip(p=1.0),
    A.ShiftScaleRotate( shift_limit=0.3, scale_limit=0.3, rotate_limit=30, p=1.0),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], always_apply=True),
    ToTensorV2()
    # ToTensor(),
])

VALID_AUG = A.Compose([
    A.Resize(100, 100, always_apply=True),
    A.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225], always_apply=True),
    ToTensorV2()
    # ToTensor(),
])


#################################################################### DATA
# Masked faces dataset
# 0 = "no mask"
# 1 = "mask"

class ClassificationDataset(Dataset):

    def __init__(self, dataFrame, subset):
        self.df = dataFrame
        
        if   subset=="train": self.tfms = TRAIN_AUG
        elif subset=="valid": self.tfms = VALID_AUG

        self.label2int = {
            "NO_MASK":  0,
            "MASK":     1,
            "BAD_MASK": 2
        }
    
    def __getitem__(self, key):

        row = self.df.iloc[key]

        ###### GET X
        raw_image = self.readImg(row["image"], method="CV2")
        aug_image = self.tfms(image=raw_image)["image"]
        
        ###### GET Y
        class_integer = self.label2int[ row["class"] ]
        class_tensor  = torch.tensor(data=class_integer, dtype=torch.long)
        
        return {"image_of_face": aug_image, "mask_class": class_tensor}

    def __len__(self):
        return len(self.df)

    def readImg(self, img_path, method="CV2"):
        if method=="PIL":
            pillow_image = Image.open(img_path)
            return np.array(pillow_image)
        elif method=="CV2":
            image = cv2.imread(img_path)
            return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            #image = cv2.imdecode(np.fromfile(row["image"], dtype=np.uint8), cv2.IMREAD_UNCHANGED)


df_path = Path("dataset/mask_df.csv")
df      = pd.read_csv(df_path)
train_df, valid_df = train_test_split(df, test_size=VALID_PCT, random_state=0, stratify=df["class"])

train_ds = ClassificationDataset(train_df, subset="train")
valid_ds = ClassificationDataset(valid_df, subset="valid")

train_dl = DataLoader(dataset     = train_ds,
                      batch_size  = BATCH_SIZE,
                      #sampler     = torch.utils.data.WeightedRandomSampler(weights = , num_samples =, replacement=True, generator=None)
                      #sampler     = catalyst.data.sampler.BalanceClassSampler(labels = , mode = "upsampling"),
                      #sampler     = catalyst.data.sampler.BalanceClassSampler(labels = , mode = "downsampling"),
                      #sampler     = catalyst.data.sampler.DynamicBalanceClassSampler(
                      num_workers = 4,
                      shuffle     = True)

valid_dl = DataLoader(dataset     = train_ds,

                      batch_size  = BATCH_SIZE,
                      num_workers = 4,
                      shuffle     = True)


#################################################################### MODEL

class ClassificationModel(nn.Module):

    def __init__(self):        
        super(ClassificationModel, self).__init__()

        self.convLayer1 = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=(3, 3), padding=(1, 1)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2)))
        
        self.convLayer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=(3, 3), padding=(1, 1)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2)))
        
        self.convLayer3 = nn.Sequential(
            nn.Conv2d(64, 128, kernel_size=(3, 3), padding=(1, 1), stride=(3,3)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2)))
        
        self.linearLayers = nn.Sequential(
            nn.Linear(in_features=2048, out_features=1024),
            nn.ReLU(),
            nn.Linear(in_features=1024, out_features=NUM_CLASES),)
        
        # Initialize layers" weights
        for sequential in [self.convLayer1, self.convLayer2, self.convLayer3, self.linearLayers]:
            for layer in sequential.children():
                if isinstance(layer, (nn.Linear, nn.Conv2d)):
                    nn.init.xavier_uniform_(layer.weight)
    
    def forward(self, x: torch.Tensor):
        out = self.convLayer1(x)
        out = self.convLayer2(out)
        out = self.convLayer3(out)
        out = out.view(-1, 2048)
        out = self.linearLayers(out)
        return out


#################################################################### TRAIN

dataloaders = {"train": train_dl, "valid": valid_dl}
model       = ClassificationModel()
#criterion   = nn.CrossEntropyLoss()
optimizer   = optim.Adam(model.parameters(), lr=MAX_LR)
scheduler   = optim.lr_scheduler.MultiStepLR(optimizer, [2])


# Create weight vector for CrossEntropyLoss
# Because the dataset is imbalanced:
# 5,000 masked faces VS 90,000 non-masked faces
pct_nomask  = len(df[ df["class"]=="NO_MASK"  ]) / len(df)
pct_mask    = len(df[ df["class"]=="MASK"     ]) / len(df)
pct_badmask = len(df[ df["class"]=="BAD_MASK" ]) / len(df)
percenteges = [pct_nomask, pct_mask, pct_badmask]
normedWeights = [1 - pct for pct in percenteges]
criterion   = nn.CrossEntropyLoss(weight=torch.tensor(normedWeights))
    


runner = catalyst.dl.SupervisedRunner(input_key="image_of_face",
                                      # output_key="logits"
                                      # loss_key="loss"
                                      target_key="mask_class")

runner.train(
    loaders    = dataloaders,
    model      = model,
    criterion  = criterion,
    optimizer  = optimizer,
    scheduler  = scheduler,
    logdir     = "./catalyst_logs",
    num_epochs = EPOCHS,
#    valid_loader="valid",
#    valid_metric="accuracy03",
#    minimize_valid_metric=False,
    verbose  = True,
# uncomment for extra metrics:
    callbacks=[
        dl.AccuracyCallback(input_key="logits", target_key="mask_class", num_classes=NUM_CLASES),
#         dl.PrecisionRecallF1SupportCallback(input_key="logits", target_key="mask_class", num_classes=NUM_CLASES),
#         dl.AUCCallback(input_key="logits", target_key="mask_class"),
         dl.ConfusionMatrixCallback(input_key="logits", target_key="mask_class", num_classes=NUM_CLASES),
    ],
)





"""
torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.MultiplicativeLR(optimizer, lr_lambda, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.StepLR(optimizer, step_size, gamma=0.1, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones, gamma=0.1, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max, eta_min=0, last_epoch=-1, verbose=False)
torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="min", factor=0.1, patience=10, threshold=0.0001, threshold_mode="rel", cooldown=0, min_lr=0, eps=1e-08, verbose=False)
torch.optim.lr_scheduler.CyclicLR(optimizer, base_lr, max_lr, step_size_up=2000, step_size_down=None, mode="triangular", gamma=1.0, scale_fn=None, scale_mode="cycle", cycle_momentum=True, base_momentum=0.8, max_momentum=0.9, last_epoch=-1, verbose=False)
"""