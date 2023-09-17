# -*- coding: utf-8 -*-
"""Diabetes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sxxTHqSfRKwkkfXUCAW3Z2i7V_gbzyjl
"""

#step 1:import library
import pandas as pd

#step 2:import data
diabetes=pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Diabetes.csv")

diabetes.info

diabetes.head

diabetes.columns

#step3 :define y and x
y=diabetes['diabetes']
x=diabetes[['pregnancies', 'glucose', 'diastolic', 'triceps', 'insulin', 'bmi',
       'dpf', 'age']]

#step4 :train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, train_size=0.7, random_state=2529)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

# step5: select the model
from sklearn.linear_model import LogisticRegression

model=LogisticRegression(max_iter=900)

model.fit(x_train,y_train)

y_pred= model.predict(x_test)
y_pred

from sklearn.metrics import accuracy_score

accuracy_score(y_test,y_pred)

