import numpy as np
import pandas as pd

arr = {
    'col1': [5, 10, 3],
    'col2': ['Tom', 'Jerry', 'Cat'],
    'col3': [100, 150, 200]
}

df = pd.DataFrame(arr)
# print(df.nunique())
# print(df.get_value(0, 'col3'))
# print(df.sort_values('col3'))
def mult(x):
    return x**2
# print(df['col1'].apply(mult))
def mult2(x):
    return x*2
# print(df.apply(mult2))
def mult(x):
    if (x > 3):
        return x**2
    else:
        return x - 10

# print(df['col1'].apply(mult))
# print(df['col1'].apply(lambda x: x*2))

