import numpy as np
import pandas as pd

# arr = np.array(['Tom', 'Jerry', 'Tony', 'Suzy', 'Johan'])
# arr2 = np.array(['Tom', 'Jerry', 'Tony', 'Suzy', 'Kris'])
# index = np.array(['a', 'b', 'c', 'd'])
# ser = pd.Series(data=arr)
# ser2 = pd.Series(data=arr2)
# ser[0] = 'Robert'
# print(ser)

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# df = pd.DataFrame(arr, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
# print(df)

arr = np.arange(0, 9).reshape(3, 3)
arr = np.random.randn(9).reshape(3, 3)
df = pd.DataFrame(arr, ['A', 'B', 'C'], ['X', 'Y', 'Z'])
# print(df.X)
# print(df.ix[['A']])
arr_new = np.arange(3)
df['V'] = arr_new
# df.drop('V', axis=1, inplace=True)
# df.reset_index(inplace=True)
# dict_new = {'V' : arr_new}
df.set_index('V', inplace=True)

# df.index = dict_new
print(df)
