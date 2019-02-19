import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
import numpy as np

df = pd.read_csv('Z-1.txt', sep='|')
# print(df)
df['Time'] = df['Time'].apply(pd.to_datetime)
df['Magnitude'] = df['Magnitude'].apply(int)
df.plot(x='Time', y='Magnitude', rot=0, figsize=(14, 10), grid=True)

state = pd.cut(df.Magnitude, bins=[-np.inf, 14, 18, 24, np.inf], labels=range(4))
cmap = plt.get_cmap('RdYlGn_r')

ax = plt.gca()  # получаем текущий объект Axes, на который ссылается ma.plot()
ax.set_xlabel('')
ax.set_ylabel('90d moving average: CBOE VIX')
ax.set_title('Volatility Regime State')
ax.grid(False)
ax.legend(loc='upper center')
ax.set_xlim(xmin=df.Time[0], xmax=df.Time[df.Time.size - 1])

trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)

# for i, color in enumerate(cmap([3, 4, 5, 6])):
#     ax.fill_between(df.Time, 2, 7, where=state == i,
#                     facecolor=color, transform=trans)

# ax.axhline(df['Magnitude'][0], linestyle='dashed', color='xkcd:dark grey',
#            alpha=0.6, label='Full-period mean', marker='')
# ax.axhline(y=5, color='r')
plt.show()
url = 'http://cnt.rm.ingv.it/en/events?starttime=1985-01-01+00%3A00%3A00&endtime=2018-06-27+23%3A59%3A59&last_nd=30&minmag=3&maxmag=10&mindepth=0&maxdepth=1000&minlat=27&maxlat=48&minlon=-7&maxlon=37.5&minversion=100&limit=50&orderby=ot-desc&tdmt_flag=-1&lat=0&lon=0&maxradiuskm=-1&wheretype=area&box_search=Mediterraneo'
vix = pd.read_csv(url, index_col=0, parse_dates=True, na_values='.',
                  infer_datetime_format=True,
                  squeeze=True).dropna()
print(vix)