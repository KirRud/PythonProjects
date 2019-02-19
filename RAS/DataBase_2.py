import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas.io.sql as pd_sql

# Можно изменять базу данных
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
Data = pd.read_csv('lvd_datah_13.dat', sep='\s+', header=None,
                   names=['Date', 'Time', 'Data_1st', 'Data_2nd', 'Data_3rd'],
                   parse_dates=['Date'])

arrDate = np.array([])
for i in range(Data['Date'].size):
    # hour = datetime.strptime(str(Data['Date'][i].year) + '-' + str(Data['Date'][i].month) + '-'
    #                      + str(Data['Date'][i].day) + ' ' + str(Data['Time'][i]), '%Y-%m-%d %H')
    hour = datetime.strptime(str(Data['Date'][i].day) + '-' + str(Data['Date'][i].month) + '-'
                             + str(Data['Date'][i].year) + ' ' + str(Data['Time'][i]), '%d-%m-%Y %H')
    # print(hour)
    arrDate = np.append(arrDate, values=[hour])

arrData_1 = np.array(Data.Data_1st)
arrData_2 = np.array(Data.Data_2nd)
arrData_3 = np.array(Data.Data_3rd)
dict_of_data = {'Date' : arrDate, 'Data_1st': arrData_1, 'Data_2nd': arrData_2, 'Data_3rd': arrData_3}
data_to_use: DataFrame = pd.DataFrame(data=dict_of_data)
data_to_use.index = data_to_use['Date']
del data_to_use['Date']
print(data_to_use)
try:
    data_to_use.to_sql(name='Data', con=conn, if_exists='append')
except (sqlite3.IntegrityError):
    print('Error')


start_date = datetime.strptime('2013-02-01', '%Y-%m-%d')
finish_date = datetime.strptime('2013-02-06 23', '%Y-%m-%d %H')
query = '''SELECT * FROM  Data WHERE Date >= \'%s\' AND Date <= \'%s\';''' % (start_date, finish_date)

print(query)
# cursor.execute(query, (start_date, finish_date))
# cursor.execute(query)
# conn.commit()
out_df = pd.read_sql_query(query, conn)
out_df['Date'] = out_df['Date'].apply(pd.to_datetime)
print(type(out_df.Date[0]))
out_df.plot(x='Date', y='Data_1st', rot=0, figsize=(14, 10), grid=True, color='red')
out_df.plot(x='Date', y='Data_2nd', grid=True, ax=plt.gca())
plt.show()
# print(cursor.fetchmany(size=arrDate.size))
# panda = pd.read_sql_query(query, con=conn)
# print(panda)



# sql = 'INSERT INTO Data1 VALUES(?, ?, ?, ?)'
# for i in range(1, data_to_use.Date.size):
#     # print(data_to_use.Date[i].get_value)
#     # cursor.executemany('''INSERT INTO Data1 VALUES(?, ?, ?, ?)''',
#     #                    (data_to_use.Date[i], data_to_use.Data_1st[i], data_to_use.Data_2nd[i],
#     #                     data_to_use.Data_3rd[i],))
#     cursor.executemany('''INSERT INTO Ex2 VALUES(?, ?, ?)''',
#                        (arrData_1[i], arrData_2[i], arrData_3[i],))
#     # print(float(data_to_use.Data_1st[i]))
#     # cursor.execute(sql, (data_to_use.Data_1st[i], ))
#
# query = 'SELECT Date FROM Data1'
# panda = pd.read_sql_query(query, con=conn)
# print(panda)
# # sql = 'DELETE FROM Data'
# # cursor.execute(sql)
# # data_to_use.to_sql(name='Data1', con=conn, if_exists='append')
# # pd_sql.to_sql(data_to_use, 'Data1', conn)
#
# # pd_sql.to_sql(data_to_use, 'Data', conn, if_exists='append')
# # query = 'SELECT Date, Data_1st, Data_2nd, Data_3rd FROM Data WHERE Date BETWEEN \"2012/05/06\" AND \"2012/06/01\"'
# # panda = pd.read_sql_query(query, con=conn)
# # data_tower = 'Data_1st'
# # panda.plot(x='Date', y=data_tower, rot=0, figsize=(14, 10), grid=True)
# # plt.show()
