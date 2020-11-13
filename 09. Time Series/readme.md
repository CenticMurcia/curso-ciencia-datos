<h1 align="center">🔮 Time Series</h1>
<h3 align="center">Dataset: <a href="https://www.kaggle.com/c/competitive-data-science-predict-future-sales">Predict future sales</a></h3>




## 🛠 Feature engeeering del tiempo

```python
# Simple
def featEng_date(df, varName):
    df['year']         = df[varName].dt.year.astype(np.int16)
    df['month']        = df[varName].dt.month.astype(np.int8)
    df['week']         = df[varName].dt.weekofyear.astype(np.int8)
    df['day_of_year']  = df[varName].dt.dayofyear.astype(np.int16)
    df['day_of_month'] = df[varName].dt.day.astype(np.int8)
    df['day_of_week']  = df[varName].dt.dayofweek.astype(np.int8)
    df['hour']         = df[varName].dt.hour.astype(np.int8)
    df['minute']       = df[varName].dt.minute.astype(np.int8)
    df['is_weekend']   = # To do
    df['is_vacation']  = # To do

# Advanced: Agregregates
periods   = ["15T", "1H", "3H"]
agregates = ["count", "mean", "std", "min", "max", "sum", "median"]
```

> - [Tsfresh](https://tsfresh.readthedocs.io): Automatic calculates time series features
> - [Trane](https://github.com/HDI-Project/Trane)




## Modelos especificos
- GAM
- ARIMA
- ARIMAX
- Facebook Prophet
- LSTM
- Fractal Analysis



---


### Introduccion

Dear all,

We want to inform you, that your final project will be to participate in a competition. The final project is due at the end of 5th week, but we advise you to start early, work throughout the course and try to apply material from each week.

At the end of the last week you will need to submit your test set predictions to Coursera grader, that will score your solution against the private part of the test set. You will also need to write a report and submit it and your code for a peer review. We advise you to check out peer-review grading criteria right now. It is located in the last week of the course. Basically, from week to week we expect you to try main concepts that we discuss in the lectures and summarize your results in a report.

The competition is hosted on Kaggle Inclass and can be found [here](https://www.kaggle.com/c/competitive-data-science-predict-future-sales) . You may also find useful the [first version of the competition](https://www.kaggle.com/c/competitive-data-science-final-project) hosted on InClass/

To start working on the final project, we now advise you to make a quick baseline and then proceed to implementing material we have discussed in this week: try several different models, preprocess and generate features for them, extract features from text. As in any other competition, your goal is to achieve the best possible quality. Good luck!




### Consejo 1

Competition data is rather challenging, so the sooner you get yourself familiar with it - the better. You can start with submitting sample_submission.csv from "Data" page on Kaggle and try submitting different constants.



### Consejo 2

A good exercise is to reproduce previous_value_benchmark . As the name suggest - in this benchmark for the each shop/item pair our predictions are just monthly sales from the previous month, i.e. October 2015.

The most important step at reproducing this score is correctly aggregating daily data and constructing monthly sales data frame. You need to get lagged values, fill NaNs with zeros and clip the values into [0,20] range. If you do it correctly, you'll get precisely 1.16777 on the public leaderboard.

Generating features like this is a necessary basis for more complex models. Also, if you decide to fit some model, don't forget to clip the target into [0,20] range, it makes a big difference.



### Consejo 3

You can get a rather good score after creating some lag-based features like in advice from previous week and feeding them into gradient boosted trees model.

Apart from item/shop pair lags you can try adding lagged values of total shop or total item sales (which are essentially mean-encodings). All of that is going to add some new information.



### Consejo 4


If you successfully made use of previous advises, it's time to move forward and incorporate some new knowledge from week 4. Here are several things you can do:

1. Try to carefully tune hyper parameters of your models, maybe there is a better set of parameters for your model out there. But don't spend too much time on it.
2. Try ensembling. Start with simple averaging of linear model and gradient boosted trees like in programming assignment notebook. And then try to use stacking.
3. Explore new features! There is a lot of useful information in the data: text descriptions, item categories, seasonal trends.


---

# Aprende a extrapolar

[Kaggle discussion](https://www.kaggle.com/questions-and-answers/72639)

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(low=-10, high=10, size=1000) # np.arange(-10, 10, 0.1)
y = np.sin(x) + np.random.normal(scale=0.2, size=x.shape)
plt.scatter(x,y, s=5)
```

Read this article: [Caution with Random Forest](https://medium.com/datadriveninvestor/why-wont-time-series-data-and-random-forests-work-very-well-together-3c9f7b271631)
