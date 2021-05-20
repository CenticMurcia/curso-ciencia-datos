<h1 align="center">Exercise</h1>


## Introduction

Today, (and the rest of the Feat. Eng. module), we are going to participate in the [predict-future-sales](https://www.kaggle.com/c/competitive-data-science-predict-future-sales) competition from Kaggle. In this competition you will work with a challenging time-series dataset consisting of daily sales data, kindly provided by one of the largest Russian software firms [1C Company](https://1c.ru/eng/title.htm). 

We are asking you to predict total sales for every product and store in the next month. By solving this competition you will be able to apply and enhance your data science skills. This is a good competition for this modeule because it has a lot feature engeniring to make:

- Data Cleaning with Missing & Outliers
- Lot of feature generation
- Extract features from text
- Combine several tables
- Work with the time and exctract lag features
- Etc.

So each day we are going to code our new knowledge from the lecture to this competition. As in any other competition, your goal is to achieve the best possible quality. Good luck!


## Exercise 1: Download the data

Go to the [data tab](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/data) of the competition, and download the data. We are going to work on our local computers, but we can work on [kaggle notebooks](https://www.kaggle.com/c/competitive-data-science-predict-future-sales/notebooks) aswell because we have 30 hours of free GPU usage each week.

Please, if you are new to kaggle watch [this video](https://www.youtube.com/watch?v=sEJHyuWKd-s)



## Exercise 2: Basic EDA

The competition data is rather challenging, so the sooner you get yourself familiar with it, the better. You can start with submitting `sample_submission.csv`. You also have to change (from sample_submission) the 0.5 and try submitting different constants. The data of the competition is the following.


- **`sales_train.csv`** Rows: 2935849 sales (January 2013 -> Octuber 2015)
  - **date**: date in format dd/mm/yyyy.
  - **date_block_num**: a consecutive month number. January 2013 is 0, February 2013 is 1,..., October 2015 is 33
  - **shop_id**: unique identifier of a shop
  - **item_id**: unique identifier of a product
  - **item_price**: current price of an item
  - **item_cnt_day**: number of products sold. You are predicting a monthly amount of this measure.
- **`shops.csv`** Rows: 60 shops
  - **shop_id**
  - **shop_name**: name of shop (RUSSIAN 🇷🇺)
- **`items.csv`** Rows: 22170 products
  - **item_id**
  - **item_name**: name of item (RUSSIAN 🇷🇺)
  - **item_category_id**: unique identifier of item category
- **`item_categories.csv`** Rows: 84 product categories
  - **item_category_id**
  - **item_category_name**: name of item category (RUSSIAN 🇷🇺)
- **`test.csv`** Rows: 214200 pairs combination of (Shop, Item)
  - **ID**: an Id that represents a (Shop, Item) tuple within the test set
  - **shop_id**
  - **item_id**


## Exercise 3

A good exercise is to reproduce previous month sales. So our predictions for each shop/item pair are just the monthly sales from the previous month (October 2015).

The most important step at reproducing this score is correctly aggregating daily data and constructing monthly sales dataframe. You need to get lagged values, fill NaNs with zeros and clip the values into [0,20] range. Generating features like this is a necessary basis for more complex models in the next days. Some hints for this exercise:

1. Filter to obtain only the sales from Octuber 2015: `date_block_num==33`
2. Do some aggregation to convert from day detail to month detail: `groupby`
3. Filter the aggregated shop-item pairs to get only the pairs needed at test: `merge`
4. Fill NaNs with zeros: `.fillna(0)`
5. Limit your predictions to the range [0,...,20]: `.clip(lower=0, upper=20)`

If you do it correctly, you'll get precisely 1.16777 on the public leaderboard.


## Submit on Eduflow

When you finish your notebook, push it to your Github repo, copy the link and submit it to the eduflow task.