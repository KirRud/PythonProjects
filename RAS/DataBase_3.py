import sqlite3
import pandas as pd
import numpy as np
from datetime import datetime
from pandas import DataFrame
import matplotlib.pyplot as plt

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
Data = pd.read_csv('lvd_datah_12.dat', sep='\s+', header=None,
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
dict_of_data = {'Date': arrDate, 'Data_1st': arrData_1, 'Data_2nd': arrData_2, 'Data_3rd': arrData_3}
data_to_use: DataFrame = pd.DataFrame(data=dict_of_data)
data_to_use.index = data_to_use['Date']
del data_to_use['Date']
# print(data_to_use)
# try:
#     data_to_use.to_sql(name='Data2', con=conn, if_exists='append')
# except (sqlite3.IntegrityError):
#     print('Error')
conn.commit()
# for i in range(data_to_use.index.size):
#     try:
#         insert = '''INSERT INTO Data2 VALUES (\'%s\', %s, %s, %s)''' % (data_to_use.index[i],
#                                                                         data_to_use.Data_1st[i],
#                                                                         data_to_use.Data_2nd[i],
#                                                                         data_to_use.Data_3rd[i])
#         cursor.execute(insert)
#         conn.commit()
#         print('?????')
#     except (sqlite3.IntegrityError):
#         update = '''UPDATE Data2 SET Data_1st = %s, Data_2nd = %s, Data_3rd = %s WHERE Date = \'%s\'''' % \
#                  (data_to_use.Data_1st[i], data_to_use.Data_2nd[i], data_to_use.Data_3rd[i], data_to_use.index[i])
#         cursor.execute(update)
#         conn.commit()
#         print('****')
#     print(i)


for i in range(data_to_use.index.size):
    upsert = '''INSERT OR REPLACE INTO Data2 (Date, Data_1st, Data_2nd, Data_3rd) VALUES (\'%s\', %s, %s, %s)''' \
             % (data_to_use.index[i], data_to_use.Data_1st[i], data_to_use.Data_2nd[i], data_to_use.Data_3rd[i])
    cursor.execute(upsert)

    print(i)
conn.commit()
start_date = datetime.strptime('2012-02-01', '%Y-%m-%d')
finish_date = datetime.strptime('2013-02-06 23', '%Y-%m-%d %H')
query = '''SELECT * FROM  Data2 WHERE Date >= \'%s\' AND Date <= \'%s\';''' % (start_date, finish_date)

out_df = pd.read_sql_query(query, conn)
out_df['Date'] = out_df['Date'].apply(pd.to_datetime)
print(out_df)
conn.close()
