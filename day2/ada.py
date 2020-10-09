# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits

from sklearn.ensemble import AdaBoostClassifier
from sklearn import tree
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np

def adaBoost(prompt, dataLoadFunction):
    print(prompt)
    X, y = dataLoadFunction(return_X_y=True)
    
    model = AdaBoostClassifier(base_estimator=tree.DecisionTreeClassifier(max_depth=5),n_estimators=50)
    scores = cross_val_score(model, X, y, cv=5)
    print('Mean accuracy:', scores.mean())


adaBoost("Dataset wine", load_wine)
adaBoost("Dataset breast cancer", load_breast_cancer)
adaBoost("Dataset handwriting", load_digits)