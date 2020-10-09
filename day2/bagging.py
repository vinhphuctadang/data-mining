# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits

from sklearn.ensemble import BaggingClassifier 
from sklearn import tree
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np

def bagging(prompt, dataLoadFunction):
    print(prompt)
    X, y = dataLoadFunction(return_X_y=True)
    
    model = BaggingClassifier(base_estimator=tree.DecisionTreeClassifier(max_depth=5),n_estimators=50) # tree has depth of 5
    scores = cross_val_score(model, X, y, cv=5)
    print('Mean accuracy:', scores.mean())


bagging("Dataset wine", load_wine)
bagging("Dataset breast cancer", load_breast_cancer)
bagging("Dataset handwriting", load_digits)