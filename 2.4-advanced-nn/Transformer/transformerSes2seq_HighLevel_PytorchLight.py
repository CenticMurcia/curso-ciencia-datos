import math
import numpy as np
import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.nn.functional as F

print("Pytorch:", torch.__version__)
print("Pytorch lightning:", pl.__version__)



############################################ DATA
#
# First, we generate simple input and output data.
#
# Input: Same as output, but with each element repeated twice.
#        [1, 1, 5, 5, 3, 3]
#
# Output: Random number sequences like [1, 5, 3]
#

N = 10000 # Number of samples (x,y sequence pairs)
S = 32    # Y sequence length. X sequence will be twice as long.
VOCAB = 128   # Number of "tokens", including 0, the "start token", and 1, the "end token"

Y = (torch.rand((N * 10, S - 2)) * (VOCAB - 2)).long() + 2  # Only generate ints in (2, 127) range
print(Y.shape)

# Make sure we only have unique rows
Y = torch.tensor(np.unique(Y, axis=0)[:N]) # [10000, 30]
X = torch.repeat_interleave(Y, 2, dim=1)   # [10000, 60]

# Add special 0 "start" and 1 "end" tokens to beginning and end
Y = torch.cat([torch.zeros((N, 1)), Y, torch.ones((N, 1))], dim=1).long() # [10000, 32]
X = torch.cat([torch.zeros((N, 1)), X, torch.ones((N, 1))], dim=1).long() # [10000, 62]



############################################ PYTORCH DATASET & DATALOADERS

BATCH_SIZE = 128
TRAIN_FRAC = 0.8

dataset = list(zip(X, Y))  # This fulfills the pytorch.utils.data.Dataset interface

# Split into train and val
num_train = int(N * TRAIN_FRAC)
num_val   = N - num_train
data_train, data_val = torch.utils.data.random_split(dataset, (num_train, num_val))

dataloader_train = torch.utils.data.DataLoader(data_train, batch_size=BATCH_SIZE)
dataloader_val   = torch.utils.data.DataLoader(data_val,   batch_size=BATCH_SIZE)

# Sample batch
x, y = next(iter(dataloader_train))
x, y



############################################ MODEL: TRANSFORMER
#
#
#
#
#

class PositionalEncoding(nn.Module):

    def __init__(self, d_model, dropout=0.1, max_len=5000):

        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0).transpose(0, 1)
        self.register_buffer('pe', pe)

    def forward(self, x):
        x = x + self.pe[:x.size(0), :]
        return self.dropout(x)


# Generate a triangular (size, size) mask.
def generate_triangular_mask(size: int):
    mask = (torch.triu(torch.ones(size, size)) == 1).transpose(0, 1)
    mask = mask.float().masked_fill(mask == 0, float('-inf')).masked_fill(mask == 1, float(0.0))
    return mask


# Classic Transformer that both encodes and decodes.
# Prediction-time inference is done greedily.
# NOTE: start token is hard-coded to be 0, end token to be 1. If changing, update predict() accordingly.
class Transformer(nn.Module):

    def __init__(self, vocab:int,
    	               max_output_length:int,
    	               dim:int = 128):

        super().__init__()

        # Parameters
        self.dim = dim
        self.max_output_length = max_output_length
        nhead = 4
        num_layers = 4
        dim_feedforward = dim

        # Encoder part
        self.embedding   = nn.Embedding(vocab, dim)
        self.pos_encoder = PositionalEncoding(d_model=self.dim)
        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer=nn.TransformerEncoderLayer(d_model = self.dim,
            	                                     nhead   = nhead,
            	                                     dim_feedforward=dim_feedforward),
            num_layers=num_layers
        )

        # Decoder part
        self.y_mask = generate_triangular_mask(self.max_output_length)
        self.transformer_decoder = nn.TransformerDecoder(
            decoder_layer=nn.TransformerDecoderLayer(d_model=self.dim, nhead=nhead, dim_feedforward=dim_feedforward),
            num_layers=num_layers
        )
        self.fc = nn.Linear(self.dim, vocab)

        # It is empirically important to initialize weights properly
        self.init_weights()
    

    def init_weights(self):
        initrange = 0.1
        self.embedding.weight.data.uniform_(-initrange, initrange)
        self.fc.bias.data.zero_()
        self.fc.weight.data.uniform_(-initrange, initrange)
      

    def forward(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        """
        Input
            x: [BS, Sx] with elements in (0...VOCAB)
            y: [BS, Sy] with elements in (0...VOCAB)
        Output
            [BS, VOCAB, Sy] logits
        """
        encoded_x = self.encode(x)  # (Sx, B, E)
        output = self.decode(y, encoded_x)  # (Sy, B, C)
        return output.permute(1, 2, 0)  # (B, C, Sy)


    def encode(self, x: torch.Tensor) -> torch.Tensor:
        # x:      [BS, Sx] with elements in (0...VOCAB)
        # Output: (Sx, B, E) embedding

        x = x.permute(1, 0)  # (Sx, B, E)
        x = self.embedding(x) * math.sqrt(self.dim)  # (Sx, B, E)
        x = self.pos_encoder(x)  # (Sx, B, E)
        x = self.transformer_encoder(x)  # (Sx, B, E)
        return x

    def decode(self, y: torch.Tensor, encoded_x: torch.Tensor) -> torch.Tensor:
        """
        Input
            encoded_x: (Sx, B, E)
            y: (B, Sy) with elements in (0, C) where C is vocab
        Output
            (Sy, B, C) logits
        """
        y = y.permute(1, 0)  # (Sy, B)
        y = self.embedding(y) * math.sqrt(self.dim)  # (Sy, B, E)
        y = self.pos_encoder(y)  # (Sy, B, E)
        Sy = y.shape[0]
        y_mask = self.y_mask[:Sy, :Sy].type_as(encoded_x)  # (Sy, Sy)
        output = self.transformer_decoder(y, encoded_x, y_mask)  # (Sy, B, E)
        output = self.fc(output)  # (Sy, B, C)
        return output

    def predict(self, x: torch.Tensor) -> torch.Tensor:
        """
        Method to use at inference time. Predict y from x one token at a time. This method is greedy
        decoding. Beam search can be used instead for a potential accuracy boost.

        Input
            x: (B, Sx) with elements in (0, C) where C is vocab
        Output
            (B, C, Sy) logits
        """
        encoded_x = self.encode(x)
        
        output_tokens = (torch.ones((x.shape[0], self.max_output_length))).type_as(x).long() # (B, max_length)
        output_tokens[:, 0] = 0  # Set start token
        for Sy in range(1, self.max_output_length):
            y = output_tokens[:, :Sy]  # (B, Sy)
            output = self.decode(y, encoded_x)  # (Sy, B, C)
            output = torch.argmax(output, dim=-1)  # (Sy, B)
            output_tokens[:, Sy] = output[-1:]  # Set the last output token
        return output_tokens


model = Transformer(vocab=C, max_output_length=y.shape[1])
logits = model(x, y[:, :-1])
print(x.shape, y.shape, logits.shape)
print(x[0:1])
print(model.predict(x[0:1]))



############################################ TRAIN (with PyTorch-Lightning)


class PL_Model(pl.LightningModule):
    """Simple PyTorch-Lightning model to train our Transformer."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.loss = nn.CrossEntropyLoss()
        self.val_acc = pl.metrics.Accuracy()

    def training_step(self, batch, batch_ind):
        x, y = batch
        # Teacher forcing: model gets input up to the last character,
        # while ground truth is from the second character onward.
        logits = self.model(x, y[:, :-1])
        loss = self.loss(logits, y[:, 1:])
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_ind):
        x, y = batch
        logits = self.model(x, y[:, :-1])
        loss = self.loss(logits, y[:, 1:])
        self.log("val_loss", loss, prog_bar=True)
        pred = self.model.predict(x)
        self.val_acc(pred, y)
        self.log("val_acc", self.val_acc, on_step=False, on_epoch=True, prog_bar=True)
    
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())


trainer = pl.Trainer(max_epochs=5,
	                 gpus=[0],
	                 callbacks=[pl.callbacks.EarlyStopping(monitor='val_loss')],
	                 progress_bar_refresh_rate=79)

trainer.fit(PL_Model(model), dataloader_train, dataloader_val)



############################################ VALIDATE

x, y = next(iter(dataloader_val))
print('Input:\n', x[:1])
print('Output:\n', y[:1])
print('Prediction:\n', model.predict(x[:1]))


