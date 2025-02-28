import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle
import os 
import sys
from src.logger import logging
from src.exception import CustomException
from datetime import datetime
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV

## Model Training Config File Path: 
x_train_logistic_path = "D:\FINALYEARPROJECTREC\artifacts\data/X_train_logistic.npy"
y_train_path = "D:\FINALYEARPROJECTREC\artifacts\data/y_train.npy"
x_test_logistic_path = "D:\FINALYEARPROJECTREC\artifacts\data/X_test_logistic.npy"
y_test_path = "D:\FINALYEARPROJECTREC\artifacts\y_test.npy"
model_save_path = 'D:\FINALYEARPROJECTREC\artifacts\logistic_regression_model.sav'

x_train_logistic = np.load(x_train_logistic_path)
y_train = np.load(y_train_path)
x_test_logistic = np.load(x_test_logistic_path)
y_test = np.load(y_test_path)

print(x_train_logistic[:10])
print(y_train[:10])
print(y_test[:10])
print(len(y_test))
print(len(y_train))


## Perform Hyperparameter Tuning With our model for Finding best params:
logging.info('perform HyperParameter Tuning with given Dataset:')

grid_serach=GridSearchCV()



# Perform Grid Search
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Print best hyperparameters
print("Best Parameters:",grid_search.best_params_)
logging.info(grid_search.best_params_)


log_model = grid_search.best_estimator_


# log_model = LogisticRegression(solver='lbfgs', max_iter=1000)
log_model.fit(x_train_logistic, y_train)

## save created model
pickle.dump(log_model, open(model_save_path, 'wb'))
logging.info('Model Create and saved Succesfully')