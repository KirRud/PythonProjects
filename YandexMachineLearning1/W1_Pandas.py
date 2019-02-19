import pandas

data = pandas.read_csv('titanic.csv', index_col='PassengerId')
male = data['Sex'].value_counts().male
female = data['Sex'].value_counts().female
with open('out1.txt', 'w') as f:
    f.write(str(male) + ' ' + str(female))
# data['str'].value_counts() выводит кол-во объектов в столбце с названием str
# в нашем случае выводится кол-во встречаний слов male and female
# relative_survived = (data['Survived'].sum() / data.shape[0]) * 100
relative_survived = (data['Survived'].sum() / len(data)) * 100
with open('out2.txt', 'w') as f:
    f.write(str(round(relative_survived, 2)))
# print(round(relative_survived, 2))
# data.shape выводит кортеж вида: (х,у), где х - кол-во строк, а у - кол-во столбцов
# print(data.shape)
# print (data['Pclass'].value_counts())
# print(data.groupby(['Pclass']).agg())
# print (data['Pclass'].value_counts().tolist())
# print (data['Pclass'].value_counts(normalize=True)*100)
countOfValues = data['Pclass'].value_counts(normalize=True).tolist()
valuesOfClass = data['Pclass'].value_counts().keys().tolist()
index = -1
for i in range(3):
    if valuesOfClass[i] == 1:
        index = i
with open('out3.txt', 'w') as f:
    f.write(str(round(countOfValues[index] * 100, 2)))
# print(round(countOfValues[index]*100,2))
medians = data['Age'].median()
# print(medians)
means = data['Age'].mean()
# print(round(means,2))
with open('out4.txt', 'w') as f:
    f.write(str(round(medians, 2)) + ' ' + str(round(means, 2)))
correl = data.corr(method='pearson').SibSp.Parch
print(round(correl, 2))
with open('out5.txt', 'w') as f:
    f.write(str(round(correl, 2)))

names = data[data.Sex == 'female']['Name'].tolist()
list_of_names = []
for name in names:
    bracket = name.find('(')
    mrs = name.find('Mrs. ')
    miss = name.find('Miss. ')
    string = ''
    if bracket != -1 and miss == -1: #если есть скобки то имя в скобках, но только при условии что нет приставки Miss
        i = bracket + 1
        while i < name.find(' ', bracket):
            string += name[i]
            i += 1
    elif mrs != -1:#если есть приставка mrs
        i = mrs + 5#аналогично смотреть ниже
        start = mrs + 5
        if name.find(' ', start) == -1:
            while i < len(name):
                string += name[i]
                i += 1
        else:
            while i < name.find(' ', start):
                string += name[i]
                i += 1
    elif miss != -1:#если есть приставка miss
        i = miss + 6#переходим на первое слово после приставки
        start = miss + 6
        if name.find(' ', start) == -1:#если это последнее слово в строке
            while i < len(name):
                string += name[i]
                i += 1
        else:
            while i < name.find(' ', start):
                string += name[i]
                i += 1
    list_of_names += [string]

dict_of_names = {}#создаем словарь в котором ключ - Имя
for name in list_of_names:
    dict_of_names.update({name: 0})

max = 0
max_key=''
for name in list_of_names:
    dict_of_names[name] += 1#каждый раз когда в списке встречается имя, в словаре значение лежащее по ключю names увел. на 1
    if dict_of_names[name] > max: # сразу находится имя которое встречается чаще всего
        max = dict_of_names[name]
        max_key = name

with open('out6.txt','w') as f:
    f.write(max_key)
with open('names2.txt', 'w') as f:
    f.write(str(list_of_names))
