#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:11:12 2018

@author: arashbarmas
"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# For prettier plots.
import seaborn
data = pd.read_csv("AmesHousing.txt", delimiter = "\t")

#%%
# splitting data to train and test sets
train = data.iloc[0:1460,]
test = data.iloc[1460:,]
data.info()
# change the predicting column to target
data.rename(columns={'SalePrice':'target'}, inplace= True)
# see the graphs to find the highest correlation
data.plot(x = "Garage Area", y= "target", style="o")
data.plot(x = "Gr Liv Area", y= "target", style="o")
data.plot(x = "Overall Cond", y= "target", style="o")
# Gr Liv Area has highest correlation
print(train[['Garage Area', 'Gr Liv Area', 'Overall Cond', 'SalePrice']].corr())

# Linear Regression, one var
lr = LinearRegression()
lr.fit(train[["Gr Liv Area"]], train[["SalePrice"]])
print(lr.coef_)
print(lr.intercept_)

a0 = lr.intercept_
a1 = lr.coef_


train_predict = lr.predict(train[["Gr Liv Area"]])
test_predict = lr.predict(test[["Gr Liv Area"]])

train_mse = mean_squared_error(train_predict, train[['SalePrice']])
test_mse = mean_squared_error(test_predict, test[['SalePrice']])

print(train_mse)
print(test_mse)

#%%
# Linear Regression, two vars
lr.fit(train[["Overall Cond", "Gr Liv Area"]], train[["SalePrice"]])
train_predict2 = lr.predict(train[["Overall Cond", "Gr Liv Area"]])
test_predict2 =  lr.predict(test[["Overall Cond", "Gr Liv Area"]])

train_mse2 = mean_squared_error(train_predict2, train[["SalePrice"]])
test_mse2 = mean_squared_error(test_predict2, test[["SalePrice"]])

print(np.sqrt(train_mse2))
print(np.sqrt(test_mse2))






