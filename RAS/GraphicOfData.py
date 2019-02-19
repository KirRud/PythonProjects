import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from pandas import DataFrame


def change_table(dif, data_to_use):
    index = 0
    difference = dif
    arr_date = np.array([])
    arr_data = np.array([])
    while index < data_to_use['Date'].size:
        arr_date = np.append(arr_date, data_to_use.Date[index])
        average = 0
        for i in range(difference):
            if index >= data_to_use.Date.size:
                break
            average += data_to_use[data_tower][index]
            index += 1
        average /= difference
        arr_data = np.append(arr_data, average)

    dict_df = {'Date': arr_date, 'Data': arr_data}
    return pd.DataFrame(data=dict_df)


Data = pd.read_csv('lvd_datah_13.dat', sep='\s+', header=None,
                   names=['Date', 'Time', 'Data_1st', 'Data_2nd', 'Data_3rd'],
                   parse_dates=['Date'])

arrDate = np.array([])
for i in range(Data['Date'].size):
    hour = datetime.strptime(str(Data['Date'][i].year) + '-' + str(Data['Date'][i].month) + '-'
                             + str(Data['Date'][i].day) + ' ' + str(Data['Time'][i]), '%Y-%m-%d %H')
    arrDate = np.append(arrDate, values=[hour])

arrData_1 = np.array(Data.Data_1st)
arrData_2 = np.array(Data.Data_2nd)
arrData_3 = np.array(Data.Data_3rd)
dict_of_data = {'Date': arrDate, 'Data_1st': arrData_1, 'Data_2nd': arrData_2, 'Data_3rd': arrData_3}
data_to_use: DataFrame = pd.DataFrame(data=dict_of_data)
#предусмотреть выбор количества точек вручную
#предусмотреть вывод землетресений по балам(предм=смотреть выбор бальности)
#и разного бала землетресения надо селать либо разного цвета либо разного размера
start_date = datetime.strptime('2013-01-01', '%Y-%m-%d')
finish_date = datetime.strptime('2018-07-01 23:59', '%Y-%m-%d %H:%M')
print(datetime.weekday(finish_date))
print('*'*100)
data_tower = 'Data_1st'
delta = finish_date - start_date
if (int(delta.days) > 7) & (int(delta.days) <= 29):
    diff = 3
    out_data = change_table(diff,data_to_use)
    out_data[(out_data.Data >= 39) & (out_data.Date >= start_date)
             & (out_data.Date <= finish_date)].plot(x='Date', y='Data', rot=0, figsize=(14, 10), grid=True, title=diff)
elif (int(delta.days) >= 30) & (int(delta.days) <= 365):
    diff = 12
    out_data = change_table(diff, data_to_use)
    # out_data[(out_data.Data >= 39) & (out_data.Date >= start_date)
    #          & (out_data.Date <= finish_date)].plot(x='Date', y='Data', rot=0
    #                                                 , figsize=(14, 10), grid=True, title=diff
    #                                                 , xlim=(start_date, finish_date))
elif int(delta.days) > 365:
    diff = 8
    out_data = change_table(diff, data_to_use)
    out_data[(out_data.Data >= 39) & (out_data.Date >= start_date)
             & (out_data.Date <= finish_date)].plot(x='Date', y='Data', rot=0, figsize=(14, 10), grid=True, title=diff)
else:
    data_to_use[(data_to_use.Data_1st >= 39) & (data_to_use.Date >= start_date)
                & (data_to_use.Date <= finish_date)].plot(x='Date', y=data_tower, rot=0, figsize=(14, 10), grid=True)
plt.show()
