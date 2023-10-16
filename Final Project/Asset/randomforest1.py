from numpy import mean
from numpy import std
from sklearn.datasets import make_regression
from sklearn.model_selection import cross_val_score, train_test_split, RepeatedKFold
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error
from matplotlib import pyplot
import pandas as pd
import numpy as np
import math
import joblib

data = pd.read_csv("dataset-alga-raw.csv")

x = data.drop(['concentration'], axis=1)
y = data['concentration']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
MAE1 = list()
MAE2 = list()
MSE1 = list()
MSE2 = list()
RMSE1 = list()
RMSE2 = list()

rfe = RFE(estimator=RandomForestRegressor(), n_features_to_select=5)
model1 = RandomForestRegressor(n_estimators=250, max_depth=2, random_state=10)
pipeline1 = Pipeline(steps=[('s',rfe),('m',model1)])

pipeline1.fit(x_train, y_train)

y_pred1 = pipeline1.predict(x_test)
y_test_arr = y_test.to_numpy()

for i in range(len(y_pred1)):
  MAE_err = abs((y_pred1[i] - y_test_arr[i]))
  MAE1.append(MAE_err)

for i in range(len(y_pred1)):
  MSE_err = pow((y_pred1[i] - y_test_arr[i]), 2)
  MSE1.append(MSE_err)

rfe_scores_mae = mean_absolute_error(y_test_arr, y_pred1)
rfe_scores_mse = mean_squared_error(y_test_arr, y_pred1)
rfe_scores_rmse = mean_squared_error(y_test_arr, y_pred1, squared=False)

print('MAE (w RFE): %.3f' % (rfe_scores_mae))
print('MSE (w RFE): %.3f' % (rfe_scores_mse))
print('RMSE (w RFE): %.3f' % (rfe_scores_rmse))

pyplot.plot(MAE1)
pyplot.xticks(ticks=[i for i in range(len(MAE1))], labels=y_pred1)
pyplot.xlabel('Predicted value')
pyplot.ylabel('Absolute Error')
pyplot.show()

pyplot.plot(MSE1)
pyplot.xticks(ticks=[i for i in range(len(MSE1))], labels=y_pred1)
pyplot.xlabel('Predicted value')
pyplot.ylabel('Squared Error')
pyplot.show()

joblib.dump(pipeline1, "./model1.pkl")