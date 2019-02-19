import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 15, 100)
date = np.arange(0, 100)
X = np.random.normal(loc=1, scale=10, size=100)
# Y = np.random.
earthquake = np.random.randint(1, 5, 20)
time_earthquake = np.linspace(0, 100, 20)
fig, ax = plt.subplots(figsize=(5, 3))
ax.stackplot(date, data, labels=('1', '2', '3'))
ax.scatter(x=time_earthquake, y=earthquake, marker='+', c='r', edgecolor='r')

fig.tight_layout()
plt.show()
plt.close('all')