import numpy as np
import pandas as pd

dict_1 = {'A': [1, 2, np.nan], 'B': [4, np.nan, np.nan], 'C': [7, 8, 9]}
df = pd.DataFrame(dict_1)
# print(df.dropna(axis=1))
df.index.names = ['Group']
# print(df.dropna(thresh=2))
#Выше для вывода без NaN, также если inplace=True то удалит строки или столбцы где кол-во nan превышает нужного
# df.fillna(10, inplace=True) #для заполнения nan
print(df.fillna(df.mean()))