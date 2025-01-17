import numpy as np  # Импортируем библиотеку NumPy для работы с массивами и матрицами.
import pandas as pd  # Импортируем pandas для работы с таблицами и данными в формате DataFrame.
from sklearn.model_selection import train_test_split  # Импортируем функцию для разделения данных на обучающую и тестовую выборки.
from sklearn.naive_bayes import GaussianNB  # Импортируем Наивный Байесовский классификатор.
from sklearn.metrics import accuracy_score, confusion_matrix  # Импортируем метрики для оценки качества модели.
import seaborn as sns  # Импортируем библиотеку Seaborn для визуализации данных.
import matplotlib.pyplot as plt  # Импортируем Matplotlib для построения графиков.
import asyncio  # Импортируем библиотеку для работы с асинхронным программированием.
import joblib  # Импортируем библиотеку для сохранения и загрузки объектов (например, моделей).
import sys  # Импортируем библиотеку sys для работы с аргументами командной строки.

np.random.seed(0)  # Устанавливаем начальное значение генератора случайных чисел для воспроизводимости результатов.

# Первый узел DAG (Это асинхронная функция, которая загружает набор данных с помощью seaborn.load_dataset(). Имя набора данных передается через командную строку с помощью sys.argv[1].)
async def load_dataset():  
    df_penguins = sns.load_dataset(sys.argv[1])  # Загружаем набор данных с помощью Seaborn, имя файла передается как первый аргумент командной строки.
    return df_penguins  # Возвращаем загруженный DataFrame.

# Это асинхронная функция, которая выполняет выборку случайных данных из переданного DataFrame df с размером выборки n
async def sample_get(df, n=150):  
    return df.sample(n)  # Возвращаем случайную выборку из DataFrame размером n (по умолчанию 150).

df = asyncio.run(sample_get(asyncio.run(load_dataset())))  # Загружаем и выбираем случайные данные асинхронно.

joblib.dump(df, sys.argv[2])  # Сохраняем выборку данных в файл, путь к файлу передается как второй аргумент командной строки.
