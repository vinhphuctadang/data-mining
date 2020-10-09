# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits
# use naive bayes
from sklearn.naive_bayes import GaussianNB 
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np

def judge(prompt, loadFunction):
    print(prompt)
    X, y = loadFunction(return_X_y=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1.0/3)

    model = GaussianNB()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    cm = confusion_matrix(y_test, y_pred)
    print('Confusion matrix:\n', cm, sep='')

judge('Training and evaluating on wine dataset...', load_wine)

judge('Training and evaluating on breast cancer dataset...', load_breast_cancer)

judge('Training and evaluating on handwriting dataset...', load_digits)

# Training and evaluating on wine dataset...
# Confusion matrix:
# [[18  0  0]
#  [ 0 27  1]
#  [ 0  0 14]]
# Training and evaluating on breast cancer dataset...
# Confusion matrix:
# [[ 66   8]
#  [  8 108]]
# Training and evaluating on handwriting dataset...
# Confusion matrix:
# [[60  0  0  0  2  0  0  1  0  0]
#  [ 0 46  0  0  0  0  1  1  5  0]
#  [ 0  2 37  2  0  0  0  0 27  0]
#  [ 0  1  1 50  0  1  0  3  4  2]
#  [ 0  0  0  0 58  1  2  7  1  0]
#  [ 0  1  0  3  0 44  0  1  2  0]
#  [ 0  0  0  0  0  1 60  0  0  0]
#  [ 0  0  0  0  0  1  0 59  1  0]
#  [ 0  2  1  1  0  2  0  2 47  0]
#  [ 1  2  0  7  0  1  0  3  7 35]]