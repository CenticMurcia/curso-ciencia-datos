---
layout: home

parent_id: 3-apps
id: 3.1-tabular
title: Tabular

img_icon: 1-table.svg
---


# Advice for Tabular data


### Neural Network

Take the longest time to train, and require extra preprocessing such as normalisation; this normalisation needs to be used at inference time as well. They can provide great results, and extrapolate well, but only if you are careful with your hyperparameters, and are careful to avoid overfitting.

<p align="center"><img width="80%" src="img/tabular2.png" /></p>

### Conclusion

We suggest starting your analysis with a random forest. This will give you a strong baseline, and you can be confident that it's a reasonable starting point. You can then use that model for feature selection and partial dependence analysis, to get a better understanding of your data.

From that foundation, you can try Gradient Boosting and Neural Nets, and if they give you significantly better results on your validation set in a reasonable amount of time, you can use them.



# Neural Nets


> ### TO-DO Read
> - [Tweet](https://twitter.com/omarsar0/status/1445839391151296512)
> - [Papers with Code Newsletter #12: Deep Learning for Tabular Data](https://paperswithcode.com/newsletter/12/) (1 July 2021)
> - Arxiv paper: [Deep Neural Networks and Tabular Data: A Survey](https://arxiv.org/abs/2110.01889)  (5 Oct 2021)


- **Factorization Machines**
  - Read [notes on matrix factorization machines](https://www.kaggle.com/residentmario/notes-on-matrix-factorization-machines)
  - Code: [LibFM in Keras](https://github.com/jfpuget/LibFM_in_Keras)
  - [TF implementation of an arbitrary order (>=2) Factorization Machine](https://github.com/geffy/tffm) based on paper Factorization Machines with libFM.
- [DeepFM](https://arxiv.org/abs/1703.04247) (Mar 2017)
- [xDeepFM](https://arxiv.org/abs/1803.05170) (Mar 2018)
- [Neural nets for Airbnb search](https://arxiv.org/abs/1810.09591) (Oct 2018)
- [TabNet](https://arxiv.org/abs/1908.07442): Attentive Interpretable Tabular Learning (Aug 2019)
- [NODE](https://arxiv.org/abs/1909.06312): Neural Oblivious Decision Ensembles for Deep Learning on Tabular Data (Sep 2019)
- [Graph NNs](https://arxiv.org/abs/2002.02046): DL on Relational DBs with Graph NNs (Feb 2020)
- [GrowNet](https://arxiv.org/abs/2002.07971): Gradient Boosting Neural Networks (Feb 2020)
   - Shallow NNs as “weak learners” in gradient boosting framework
   - Incorporates 2nd order stats, corrective step & dynamic boost rate to remedy pitfalls of gradient boosting tree
   - Outperforms XGBoost
- [TabTransformer](https://arxiv.org/abs/2012.06678): Tabular Data Modeling Using Contextual Embeddings (Dec 2020)
- Idea mia: Residual conecctions on MLP ???
- Frameworks
  - [DeepTables](https://deeptables.readthedocs.io/en/latest/models.html)
  - [Pytorch tabular](https://github.com/manujosephv/pytorch_tabular)
  - [Microsoft hummingbird](https://github.com/microsoft/hummingbird): Convert trees to NNs


# Datasets

- UCI
  - [Adult](http://archive.ics.uci.edu/ml/datasets/Adult) Binary Classification
  - [Glass Identification](http://archive.ics.uci.edu/ml/datasets/Glass+Identification) Multi-class Classification
- Sklearn atasets
  - [Boston](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html) regression, 506 samples
- Kaggle competitions
  - [Rossmann](https://www.kaggle.com/c/rossmann-store-sales)
  - [Porto Seguro](https://www.kaggle.com/c/porto-seguro-safe-driver-prediction)
  - [Bulldozers](https://www.kaggle.com/c/bluebook-for-bulldozers)

# Benchmark

- https://forums.fast.ai/t/tabnet-with-fastai-v2/62600/19
- https://forums.fast.ai/t/some-baselines-for-other-tabular-datasets-with-fastai2/62627
- https://github.com/muellerzr/fastai2-Tabular-Baselines


<h1 align="center">Temporal Series</h1>

# ➕ Feature engineering

#### Get information about the current date (date variable)

|     Date     | | Day | Month | Year | Weekday | Weeknum | IsHoliday |
|:------------:|-|:---:|:-----:|:----:|:-------:|:-------:|:---------:|
| **1/1/2018** | |  1  |   1   | 2018 |    2    |    1    |     1     |
| **2/1/2018** | |  2  |   1   | 2018 |    3    |    1    |     0     |
| **3/1/2018** | |  3  |   1   | 2018 |    4    |    1    |     0     |
| **4/1/2018** | |  4  |   1   | 2018 |    5    |    1    |     0     |
| **5/1/2018** | |  5  |   1   | 2018 |    6    |    1    |     0     |
| **6/1/2018** | |  6  |   1   | 2018 |    7    |    1    |     0     |
| **7/1/2018** | |  7  |   1   | 2018 |    1    |    2    |     0     |
| **8/1/2018** | |  8  |   1   | 2018 |    2    |    2    |     0     |
| **9/1/2018** | |  9  |   1   | 2018 |    3    |    2    |     0     |


#### Get information about the past (continuous variable)

|     Date     |  Sales  | | Lag1 | Lag2 | Moving average (2) |
|:------------:|:-------:|-|:----:|:----:|:--------------:|
| **1/1/2018** | **100** | |   -  |   -  |        -       |
| **2/1/2018** | **150** | |  100 |   -  |       100      |
| **3/1/2018** | **160** | |  150 |  100 |       125      |
| **4/1/2018** | **200** | |  160 |  150 |       155      |
| **5/1/2018** | **210** | |  200 |  160 |       180      |
| **6/1/2018** | **150** | |  210 |  200 |       205      |
| **7/1/2018** | **160** | |  150 |  210 |       180      |
| **8/1/2018** | **120** | |  160 |  150 |       155      |
| **9/1/2018** |  **80** | |  120 |  160 |       140      |


- Lag variables (autoregressive elements)
- Aggregated features on lagged variables:
  - Moving Average (MA): Average of Lags.
  - Exponential Weighting Moving Average (EWMA): More recent values have higher weight.
  - Others like mean, std, sum, substraction
  - Regression on lags (slope, intercep)

---

# Reference
- Time Series in Driverless AI
  - [documentation](http://docs.h2o.ai/driverless-ai/latest-stable/docs/userguide/time-series.html)
  - [video](https://youtu.be/eF4Oa0ZzXdQ)
- MLcourse.ai  Time series analysis (Topic 9)
  - [Part 1](https://mlcourse.ai/articles/topic9-part1-time-series)
  - [Part 2: Facebook Prophet](https://mlcourse.ai/articles/topic9-part2-prophet)
