import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Создадим словарь с двумя наборами данных. Пишем:

data = { 'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
         'математика': [4, 5, 4, 5, 5, 3, 5, 4, 5, 4],
         'физика': [4, 5, 4, 5, 3, 4, 5, 4, 5, 4],
         'химия': [4, 5, 4, 5, 5, 4, 5, 4, 5, 5],
         "биология": [5, 3, 4, 5, 5, 4, 5, 4, 5, 5],
         "история": [5, 5, 4, 5, 5, 4, 5, 4, 5, 4],
         }

#Создаём датафрейм:
df = pd.DataFrame(data)

print(df.head())

print(df)

print(f'Средняя оценка учеников по математике - {df["математика"].mean()}')
print(f'Средняя оценка учеников по физике - {df["физика"].mean()}')
print(f'Средняя оценка учеников по химии - {df["химия"].mean()}')
print(f'Средняя оценка учеников по биологии - {df["биология"].mean()}')
print(f'Средняя оценка учеников по истории - {df["история"].mean()}')

print(f'Медианная оценка учеников по математике - {df["математика"].median()}')
print(f'Медианная оценка учеников по физике - {df["физика"].median()}')
print(f'Медианная оценка учеников по химии - {df["химия"].median()}')
print(f'Медианная оценка учеников по биологии - {df["биология"].median()}')
print(f'Медианная оценка учеников по истории - {df["история"].median()}')

Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)

IQR = Q3_math - Q1_math
dounside = Q1_math - 1,5*IQR
upside = Q3_math + 1,5*IQR

data_math = {'value' : [4, 5, 4, 5, 5, 3, 5, 4, 5, 4]}
df = pd.DataFrame(data_math)

df['value'].hist()
plt.show()