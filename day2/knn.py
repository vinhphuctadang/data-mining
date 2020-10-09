# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits
# use knn
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import KFold, cross_val_score, train_test_split
import numpy as np

def cancer():
    print('Considering Breast cancer dataset ...')
    # load data (using predefined function from sklearn)
    X, y = load_breast_cancer(return_X_y=True, as_frame=True)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) #print(X_train.shape, y_train.shape)
    for foldCount in range(2, 6):
        print('Going to use %d-fold cross validation' % foldCount)
        # new model
        model = KNeighborsClassifier(n_neighbors=3)
        # cross_val_score will automatically split data and train data, which will returns accuracy scores reguarding the fold count
        scores = cross_val_score(model, X, y, cv=foldCount)
        # output
        print('--> Mean accuracy scores:', np.mean(scores))

    # Going to use 2-fold cross validation
    # --> Mean accuracy scores: 0.9156535705460835
    # Going to use 3-fold cross validation
    # --> Mean accuracy scores: 0.9209041121321823
    # Going to use 4-fold cross validation
    # --> Mean accuracy scores: 0.926253324140648
    # Going to use 5-fold cross validation
    # --> Mean accuracy scores: 0.9191429902189101

def wine():
    print('Considering wine dataset ...')
    X, y = load_wine(return_X_y=True, as_frame=True)
    for foldCount in range(2, 6):
        print('Going to use %d-fold cross validation' % foldCount)
        model = KNeighborsClassifier(n_neighbors=3)
        scores = cross_val_score(model, X, y, cv=foldCount)
        # output
        print('--> Mean accuracy scores:', np.mean(scores))
# Going to use 2-fold cross validation
# --> Mean accuracy scores: 0.6629213483146067
# Going to use 3-fold cross validation
# --> Mean accuracy scores: 0.6631826741996234
# Going to use 4-fold cross validation
# --> Mean accuracy scores: 0.6856060606060606
# Going to use 5-fold cross validation
# --> Mean accuracy scores: 0.6912698412698413

def handwriting():
    print('Considering handwriting dataset ...')
    X, y = load_digits(return_X_y=True, as_frame=True)
    for foldCount in range(2, 6):
        print('Going to use %d-fold cross validation' % foldCount)
        model = KNeighborsClassifier(n_neighbors=3)
        scores = cross_val_score(model, X, y, cv=foldCount)
        # output
        print('--> Mean accuracy scores:', np.mean(scores))

cancer()
wine()
handwriting()