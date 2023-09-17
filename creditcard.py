# -*- coding: utf-8 -*-
"""CreditCard.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14R85uT0p6N2EMsgesYe8BcQHHfwjq2Oo
"""

import pandas as pd

default = pd.read_csv("https://github.com/YBI-Foundation/Dataset/raw/main/Credit%20Default.csv")

default.head

default.describe

default.columns

default['Default'].value_counts()

y = default['Default']
x = default.drop(['Default'],axis=1)

y.shape

x.shape

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7,random_state=2528)

x_train.shape,x_test.shape,y_train.shape,y_test.shape

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()

model.fit(x_train,y_train)

model.intercept_

model.coef_

y_pred = model.predict(x_test)

y_pred

from sklearn.metrics import confusion_matrix, accuracy_score

confusion_matrix(y_test,y_pred)

accuracy_score(y_test,y_pred)

