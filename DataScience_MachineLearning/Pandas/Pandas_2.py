import numpy as np
import pandas as pd

index1 = np.array(['G1', 'G1', 'G1', 'G2', 'G2', 'G3'])
index2 = np.array([1, 2, 3, 1, 2, 3])

mix_index = list(zip(index1, index2))
mix_index = pd.MultiIndex.from_tuples(mix_index)
# mix_index = pd.MultiIndex.from_tuples(index1, index2)

df = pd.DataFrame(np.random.randn(6, 3), mix_index, ['A', 'B', 'C'])
df.index.names = ['Group', 'Index']
print(df)
print('\n')
# print(df.loc['G1']['A'])