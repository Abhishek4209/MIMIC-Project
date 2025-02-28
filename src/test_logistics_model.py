import numpy as np
from sklearn.metrics import roc_auc_score, average_precision_score
import pickle
from src.exception import CustomException
from src.logger import logging
import os 
import sys
from datetime import datetie 

## Model File Config Path:
x_train_logistic_path = "D:\FINALYEARPROJECTREC\artifacts\X_train_logistic.npy"
y_train_path = "D:\FINALYEARPROJECTREC\artifacts\y_train.npy"
x_test_logistic_path = "D:\FINALYEARPROJECTREC\artifacts\X_test_logistic.npy"
y_test_path = "D:\FINALYEARPROJECTREC\artifacts\y_test.npy"
model_save_path = 'D:\FINALYEARPROJECTREC\artifacts\logistic_regression_model.sav'


x_train_logistic = np.load(x_train_logistic_path)
y_train = np.load(y_train_path)
x_test_logistic = np.load(x_test_logistic_path)
y_test = np.load(y_test_path)


## load trained model
loaded_model = pickle.load(open(model_save_path, 'rb'))
logging.info('Load trained model file succesfully...')



train_predictions = loaded_model.predict_proba(x_train_logistic)[:, 1]
test_predictions = loaded_model.predict_proba(x_test_logistic)[:, 1]

train_auroc = roc_auc_score(y_train, train_predictions)
test_auroc = roc_auc_score(y_test, test_predictions)
train_auprc = average_precision_score(y_train, train_predictions)
test_auprc = average_precision_score(y_test, test_predictions)
logging.info('ROC AUC Score is calculated Succesfully...')


logging.info('AUROC AUPRC AUROC AUPRC Curve')
print("LOGISTIC REGRESSION TRAIN AUROC: ", train_auroc)
print("LOGISTIC REGRESSION TRAIN AUPRC: ", train_auprc)
print("LOGISTIC REGRESSION TEST AUROC: ", test_auroc)
print("LOGISTIC REGRESSION TEST AUPRC: ", test_auprc)


logging.info('Open')
with open('./abhishek_logistic_regression.txt', 'w') as f:
    f.write(f'{train_auroc:.4f}\n')
    f.write(f'{train_auprc:.4f}\n')
    f.write(f'{test_auroc:.4f}\n')
    f.write(f'{test_auprc:.4f}\n')
