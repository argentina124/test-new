# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 08:36:47 2022

@author: dhpcap
"""
import sklearn
from sklearn import datasets
dataset = datasets.load_wine()
print("input: ", dataset.feature_names)
print("Outputs: ", dataset.target_names)

print(dataset.data[0:3])
print(dataset.target)

from sklearn.model_selection import train_test_split
inputs= dataset.data
outputs =dataset.target
X_train, X_test, y_train, y_test = train_test_split(inputs,outputs,test_size=0.3,random_state=1)

from sklearn.naive_bayes import GaussianNB
classifer =GaussianNB()
classifer.fit(X_train, y_train)
y_pred = classifer.predict(X_test)

from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

import seaborn as sns
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True)

