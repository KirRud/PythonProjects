import numpy as np
import pandas as pd

arr1 = {
    'A': ['A1', 'A2', 'A3'],
    'B': ['B1', 'B2', 'B3']
}
df1 = pd.DataFrame(arr1, index=[1, 2, 3])

arr2 = {
    'C': ['C1', 'C2', 'C3'],
    'D': ['D1', 'D2', 'D3']
}
df2 = pd.DataFrame(arr2, index=[1, 2, 3])

arr3 = {
    'E': ['E1', 'E2', 'E3'],
    'F': ['F1', 'F2', 'F3']
}
df3 = pd.DataFrame(arr3, index=[1, 2, 3])

df_1 = pd.concat([df1, df2, df3], axis=1)
df_2 = pd.concat([df1, df2, df3], axis=0)
df_2.reset_index()
# print(df_1)
# print(df_2)

left = pd.DataFrame({
    'A': ['A1', 'A2', 'A3'],
    'B': ['B1', 'B2', 'B3'],
    'key': ['K1', 'K2', 'K3']
}, index=[1, 2, 3])

right = pd.DataFrame({
    'C': ['C1', 'C2', 'C3'],
    'D': ['D1', 'D2', 'D3'],
    'key': ['K1', 'K2', 'K4']
}, index=[1, 2, 3])

df_mid_1 = pd.merge(left, right, how='inner', on='key')
df_mid_2 = pd.merge(left, right, how='left', on='key')
df_mid_3 = pd.merge(left, right, how='right', on='key')
df_mid_4= pd.merge(left, right, how='outer', on='key')
# print(df_mid_1)
# print(df_mid_2)
# print(df_mid_3)
# print(df_mid_4)

left = pd.DataFrame({
    'A': ['A1', 'A2', 'A3'],
    'B': ['B1', 'B2', 'B3'],
    'key': ['K1', 'K2', 'K3']
}, index=[1, 2, 3])

right = pd.DataFrame({
    'C': ['C1', 'C2', 'C3'],
    'D': ['D1', 'D2', 'D3'],
    'key': ['K1', 'K2', 'K4']
}, index=[1, 2, 3])
df_join = left.join(right.set_index('key'), on='key', how='outer')
print(df_join)
