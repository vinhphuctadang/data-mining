# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits

from sklearn import svm 
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np


def judge(prompt, loadFunction):
    print(prompt)
    X, y = loadFunction(return_X_y=True)

    for kernel in ('rbf', 'poly', 'sigmoid'):
        model = svm.SVC(kernel=kernel)
        scores = cross_val_score(model, X, y, cv=5) # run 5 folds
        print('Mean accuracy using kernel %s:' % kernel, scores.mean())


judge('Applying Svm on wine', load_wine)
judge('Applying Svm on breast cancer', load_breast_cancer)
judge('Applying Svm on handwriting', load_digits)
