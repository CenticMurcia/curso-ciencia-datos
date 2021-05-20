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


#### My custom `BalanceClassSampler` inspired from the catalyst one

```python
class BalanceClassSampler(torch.utils.data.Sampler):
    """
    Allows you to create stratified sample on unbalanced classes.
    Inspired from Catalyst's BalanceClassSampler:
    https://catalyst-team.github.io/catalyst/_modules/catalyst/data/sampler.html#BalanceClassSampler

    Args:
        labels: list of class label for each elem in the dataset
        mode: Strategy to balance classes. Must be one of [downsampling, upsampling]
    """

    def __init__(self, labels:list[int], mode:str = "upsampling"):

        labels = np.array(labels)
        self.unique_labels = set(labels)

        ########## STEP 1:
        # Compute the final_num_samples_per_label (an Integer)
        num_samples_per_label = {label: (labels == label).sum() for label in self.unique_labels}

        if   mode == "upsampling":   self.final_num_samples_per_label = max(num_samples_per_label.values())
        elif mode == "downsampling": self.final_num_samples_per_label = min(num_samples_per_label.values())
        else:                        raise Exception("mode should be: \"downsampling\" or \"upsampling\"")

        ########## STEP 2:
        # Compute actual indices of every label.
        # A Diccionary of lists
        self.indices_per_label = {label: np.arange(len(labels))[labels==label].tolist() for label in self.unique_labels}


    def __iter__(self): #-> Iterator[int]:

        indices = []
        for label in self.unique_labels:

            label_indices = self.indices_per_label[label]

            repeat_all_elementes  = self.final_num_samples_per_label // len(label_indices)
            pick_random_elementes = self.final_num_samples_per_label %  len(label_indices)

            indices += label_indices * repeat_all_elementes # repeat the list several times
            indices += random.sample(label_indices, k=pick_random_elementes)  # pick last elements randomly (without repetition)

        assert len(indices) == self.__len__()
        np.random.shuffle(indices) # Inplace shuffle the list

        return iter(indices)
    

    def __len__(self) -> int:
        return self.final_num_samples_per_label * len(self.unique_labels)
```


