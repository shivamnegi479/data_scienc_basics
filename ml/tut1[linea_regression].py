import numpy as np
import pandas as pd
from sklearn import datasets,linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
diabtities=datasets.load_diabetes()
# ['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# print(diabtities.keys())
# new = pd.DataFrame.from_dict(diabtities)

data_nex=diabtities.data[:,np.newaxis,2]

diabtities_x_train=data_nex[:-30]

diabtities_x_test=data_nex[-30:]

diabtities_y_train=diabtities.target[:-30]

diabtities_y_test=diabtities.target[-30:]

model=linear_model.LinearRegression()

model.fit(diabtities_x_train,diabtities_y_train)

x_predict=model.predict(diabtities_x_test)

print("Mean Squad error of model is",mean_squared_error(diabtities_x_test,x_predict))

