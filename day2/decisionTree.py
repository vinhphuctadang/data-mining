# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn
from sklearn.datasets import load_breast_cancer, load_wine, load_digits
from sklearn import tree
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np

def judge(prompt, loadFunction):
    print(prompt)
    X, y = loadFunction(return_X_y=True)
    for criterion in ('gini', 'entropy'): 
        for max_depth in range(3, 6):
            print('Using decision tree with criterion="%s", maxdep=%s' % (criterion, max_depth))
            model = tree.DecisionTreeClassifier(criterion=criterion, max_depth=max_depth)
            foldCount = 5
            scores = cross_val_score(model, X, y, cv=foldCount)
            print('Mean accuracy over %d-fold cross-validation:'%foldCount, scores.mean(),'\n')


judge('------------\nConsider wine dataset:', load_wine)

judge('------------\nConsider breast cancer dataset:', load_)

judge('------------\nConsider handwriting dataset:', load_digits)

# ------------
# Consider wine dataset:
# Using decision tree with criterion="gini", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.8931746031746032
# Using decision tree with criterion="gini", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8993650793650794
# Using decision tree with criterion="gini", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.8931746031746032
# Using decision tree with criterion="entropy", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.9046031746031747
# Using decision tree with criterion="entropy", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8934920634920633
# Using decision tree with criterion="entropy", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.9046031746031747
# tadangvinhphuc@dangs-MacBook-Pro day2 % python3 decisionTree.py
# ------------
# Consider wine dataset:
# Using decision tree with criterion="gini", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.8820634920634921 

# Using decision tree with criterion="gini", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8992063492063492 

# Using decision tree with criterion="gini", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.8765079365079365 

# Using decision tree with criterion="entropy", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.8934920634920633 

# Using decision tree with criterion="entropy", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8934920634920633 

# Using decision tree with criterion="entropy", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.8880952380952379 

# python3 decisionTree.py
# ------------
# Consider wine dataset:
# Using decision tree with criterion="gini", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.8707936507936509 

# Using decision tree with criterion="gini", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8993650793650791 

# Using decision tree with criterion="gini", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.8876190476190475 

# Using decision tree with criterion="entropy", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.9046031746031747 

# Using decision tree with criterion="entropy", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.8934920634920633 

# Using decision tree with criterion="entropy", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.8990476190476191 

# ------------
# Consider breast cancer dataset:
# Using decision tree with criterion="gini", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.9226207110697097 

# Using decision tree with criterion="gini", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.927899394503959 

# Using decision tree with criterion="gini", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.9208973761838223 

# Using decision tree with criterion="entropy", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.9332557056357709 

# Using decision tree with criterion="entropy", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.9402577239559076 

# Using decision tree with criterion="entropy", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.9402577239559076 

# ------------
# Consider handwriting dataset:
# Using decision tree with criterion="gini", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.43297431135871245 

# Using decision tree with criterion="gini", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.547638502011761 

# Using decision tree with criterion="gini", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.6272361497988239 

# Using decision tree with criterion="entropy", maxdep=3
# Mean accuracy over 5-fold cross-validation: 0.503060971835345 

# Using decision tree with criterion="entropy", maxdep=4
# Mean accuracy over 5-fold cross-validation: 0.6310708758898175 

# Using decision tree with criterion="entropy", maxdep=5
# Mean accuracy over 5-fold cross-validation: 0.7312689569792633 