import numpy as np
import pandas as pd

data = {
    'Company': ['Google', 'Google', 'FB', 'FB', 'Kite', 'Kite'],
    'Person': ['Alex', 'Sophie', 'Marry', 'Erza', 'Yesk', 'Zhanibok'],
    'Sales': [100, 120, 130, 100, 120, 130],
    'Rating': [5, 2, 3, 4, 2, 3]
}
df = pd.DataFrame(data)
print(df.groupby('Company').mean())
print(df.groupby('Company').max())
print(df.groupby('Company').std())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().loc['FB']['Sales'])