from posixpath import supports_unicode_filenames
import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from openpyxl.workbook import Workbook
from openpyxl import load_workbook

df1 = pd.read_excel('1.xlsx')
data1 = df1[['Feed Temperature', 'Feed Rate', 'Dist. Comp.', 'Bottom Comp.', 'Efficiency']]
x_test = [data1.iloc[0,0:4].values]
y_test = data1.iloc[0,4].reshape(-1, 1)



print(x_test, y_test)

df = pd.read_excel('exergy_data.xlsx')
data = df[['Feed Temperature', 'Feed Rate', 'Dist. Comp.', 'Bottom Comp.', 'Efficiency']]

x = data.iloc[0:200,0:4].values
y = data.iloc[0:200, 4].values



scaler_x = StandardScaler().fit(x)

reshaped_Y = y.reshape(len(y), 1)
scaler_y = StandardScaler().fit(reshaped_Y)

# reshaped_X = x.reshape(-1, 1)
scaled_x_test = scaler_x.transform(x_test)
print(scaled_x_test)

scaled_y_test = scaler_y.transform(y_test)
print(scaled_y_test)

model = load_model('models\methanol_water_exergy_efficiency.h5')
model.summary

prediction = scaler_y.inverse_transform(model.predict(scaled_x_test))
print(prediction)



