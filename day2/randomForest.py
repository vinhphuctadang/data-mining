# import pandas to read csv and manipulate dataframes
import pandas as pd
import sklearn

# prepared data
from sklearn.datasets import load_breast_cancer, load_wine, load_digits
# import models 
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.metrics import confusion_matrix

import numpy as np

def randomForest(prompt, dataLoadFunction):
    print(prompt)
    X, y = dataLoadFunction(return_X_y=True, as_frame=True)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3)

    # prepare model
    model = RandomForestClassifier(n_estimators=50)

    # train
    model.fit(X_train, y_train)

    # evaluate acc
    print('Accuracy:', model.score(X_test, y_test))

    # plot
    import matplotlib.pyplot as plt 
    plt.suptitle(prompt)
    plt.barh(X.columns, model.feature_importances_) # draw horizontal bar chart
    plt.show()

randomForest("Feature importances of dataset wine", load_wine)
randomForest("Feature importances of dataset breast cancer", load_breast_cancer)
randomForest("Feature importances of dataset handwriting", load_digits)