<h1 align="center">Unbalanced Datasets</h1>

## Motivation

Classification problems with few data for some classes.


## Solutions

If you can not get more data of the underrepresented classes, you can fix the imbalance with code:

- Fix it on the **dataloader `sampler`**:
  - Weighted Random Sampler
    - `torch.utils.data.WeightedRandomSampler(weights=[…])`
  - **Subsample majority class**. But you can lose important data.
    - `catalyst.data.sampler.BalanceClassSampler(labels=ds.targets, mode="downsampling")`
  - **Oversample minority class**. But you can overfit.
    - `catalyst.data.sampler.BalanceClassSampler(labels=ds.targets, mode="upsampling")`
- Fix it on the **loss function**:
  - `CrossEntropyLoss(weight=[…])`


#### How to compute the class weights?




