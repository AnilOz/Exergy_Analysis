import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import threading
from openpyxl import load_workbook
from openpyxl import Workbook


wb1 = load_workbook('1.xlsx')
ws1 = wb1.active


labels = [x.value for cell in ws1['A1':'AC1'] for x in cell]
print(labels)

df = pd.read_excel("dataraw.xlsx")
df.columns = labels
df.drop_duplicates(subset ="Distillate Enthalpy",
                     keep = 'first', inplace = True)

df.to_excel('exergy_data.xlsx')

print(df)
        