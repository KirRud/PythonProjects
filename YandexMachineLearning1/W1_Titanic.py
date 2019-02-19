from pandas import read_csv, DataFrame, Series
import numpy as np
from sklearn.tree import DecisionTreeClassifier

def sex(x):
    if x == 'female':
        x = 1
    elif x == 'male':
        x = 0
    return x

data = read_csv('titanic.csv', index_col='PassengerId')
data.dropna(axis=0, how='any', subset=['Age'], inplace=True)
survived_people = np.array(data.Survived)
data.drop(['Survived', 'Name', 'SibSp', 'Parch', 'Ticket', 'Cabin', 'Embarked'], axis=1, inplace=True)
data['Sex'] = data['Sex'].apply(sex)

clf = DecisionTreeClassifier(random_state=241)
clf.fit(data, survived_people)
impotances = clf.feature_importances_
print(data.columns)
print(impotances)
with open('out.txt', 'w') as fin:
    fin.write('Fare Sex')
