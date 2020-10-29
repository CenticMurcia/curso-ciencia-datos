<p align="center"><img src="../img/miniaturas YT/3-Linear.png" height="200px"></p>


1. **Linear Regression**
   - How to split the data between training and test
   - Ordinary Least Squares
   - Analyzing the results of the model
2. **Logistic Regression** (Linear regression for classification)
   - Sigmoid function
3. **Regulated linear models** (Penalized regression)
   - LASSO Regression (L1 Regularization)
   - Ridge Regression (L2 Regularization)
   - ElasticNet Regression (L1 & L2 Regularization)
4. **Non linear modifications**
   - Polynomial Regression
   - Generalized Linear Model (GLM) [H20 doc](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glm.html)
   - Generalized Additive Models (GAM) [H20 doc](https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gam.html)
5. **SGD**
   - Perceptron
   - Vowpal Wabbit

---

## 3.1 Linear Regression

![](img/xkcd_meme.png)

Linear Regression is a parametric model which predicts a continuous outcome feature (**Y**) from one or more explanatory features (**X**).  

**Y** = beta_0 + beta_1 * **X**

$$
\sum_n (x)
$$

beta_0 is called the intercept term, and represents the expected mean value of Y when all explanatory features equal 0.  
beta_1 is called a beta coefficient, and represents the expected change in the value of Y that results from a one unit change in X.

This is module fits a straight line to your data, where the value of the outcome feature can be calculated as a linear combination of the explanatory features. Sounds relatively simple? Afraid not, there are many nuances and conditions that need to be understood before using linear regression! We are going to delve into these assumptions and conditions and then demonstrate how to use this algorithm on the kiva dataset.


### Resources
- [Comprehensive Guide to Regression](https://www.analyticsvidhya.com/blog/2015/08/comprehensive-guide-regression/)
- [Understanding key regression statistics](http://connor-johnson.com/2014/02/18/linear-regression-with-python/)


## 3.2 Logistic regression

Logistic regression is very similar to linear regression but has a categorical outcome instead. So rather than modeling a continuous dependent variable, it models a binary classification - yes or no, true or false, 1 or 0. This is still a linear model as it assumes a linear relationship between the independent variables and the link function.  

To learn more about Logistic Regression, try to following resources:
- [Beginners guide to Logistic Regression](https://www.analyticsvidhya.com/blog/2015/11/beginners-guide-on-logistic-regression-in-r/): A good overview of the theory and mathematics behind the algorithm
- [Logistic Regression in Python](http://blog.yhat.com/posts/logistic-regression-python-rodeo.html): A thorough tutorial on a publicly available dataset in Python


## 3.3 Regulated linear models
Both linear and logistic regression have a tendancy to overfit when there are a large number of features. Therefore it is important that we choose the features which have the most predictive power but how do we choose these features? We can use our EDA to a certain extent but that only goes so far.

This is where ridge and lasso regularization techniques come into play! Both of these techniques can be used to identify which features explain the most variance and should therefore be kept in the model.

To learn more about ridge and lasso regression and general regulaization techniques, we recommend the following resources:
- [Complete tutorial on ridge and lasso regression in python](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/): A broad tutorial explaining why we use regularization techniques, touching on the mathematics behind the algorithms and giving a few examples in python.
- [An Introduction to Statistical Learning, Chapter 6.2](http://www-bcf.usc.edu/%7Egareth/ISL/ISLR%20Sixth%20Printing.pdf): A comprehensive explanation of both Lasso and Ridge and their application in the context of statistical learning.

