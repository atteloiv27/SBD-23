from airflow import DAG  # Импортируем DAG из Airflow для создания рабочего процесса.
from airflow.operators.python import PythonOperator  # Импортируем оператор для выполнения Python-функций в DAG.
from datetime import datetime  # Импортируем модуль для работы с датами и временем.
from sklearn.datasets import load_wine  # Импортируем функцию для загрузки датасета "Вино".
from sklearn.model_selection import train_test_split  # Импортируем функцию для разделения данных на обучающие и тестовые выборки.
from sklearn.metrics import mean_absolute_error, r2_score  # Импортируем метрики для оценки модели.
import numpy as np  # Импортируем библиотеку для работы с массивами и случайными числами.
import matplotlib.pyplot as plt  # Импортируем библиотеку для визуализации данных.
from graphviz import Digraph  # Импортируем библиотеку для рисования графов (DAG).
import os  # Импортируем библиотеку для работы с операционной системой (например, для проверки существования файлов).

# Функция для загрузки данных
def load_data():
    print("Загрузка данных.")  # Печатаем сообщение о начале загрузки данных.
    wine = load_wine()  # Загружаем датасет "Вино".
    data = wine.data  # Извлекаем данные (признаки).
    target = wine.target  # Извлекаем целевые значения (целевая переменная).
    print(f"Данные успешно загружены. Размер данных: {data.shape}")  # Печатаем размер данных.
    return data, target  # Возвращаем данные и целевые значения.

# Функция для нормализации данных
def normalize_data(data):
    print("Нормализация данных.")  # Печатаем сообщение о начале нормализации.
    data_normalized = (data - np.mean(data, axis=0)) / np.std(data, axis=0)  # Стандартизируем данные.
    print("Нормализация завершена.")  # Печатаем сообщение о завершении нормализации.
    return data_normalized  # Возвращаем нормализованные данные.

# Функция для разделения данных на обучающую и тестовую выборки
def split_data(data, target):
    print("Разделение данных на обучающую и тестовую выборки.")  # Печатаем сообщение о начале разделения данных.
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=1)  # Разделяем данные.
    print("Разделение завершено.")  # Печатаем сообщение о завершении разделения.
    return X_train, X_test, y_train, y_test  # Возвращаем разделенные данные.

# Функция для применения метода наименьших квадратов (МНК)
def apply_least_squares(X_train, y_train):
    print("Применение метода наименьших квадратов.")  # Печатаем сообщение о начале применения МНК.
    X = np.c_[np.ones(X_train.shape[0]), X_train]  # Добавляем единичный столбец для учета свободного члена.
    theta = np.linalg.inv(X.T @ X) @ X.T @ y_train  # Вычисляем параметры модели методом наименьших квадратов.
    print("МНК завершен. Параметры: ", theta)  # Печатаем параметры модели.
    return theta  # Возвращаем параметры модели.

# Функция для анализа результатов
def analyze_results(X_test, y_test, theta):
    print("Анализ результатов.")  # Печатаем сообщение о начале анализа.
    X = np.c_[np.ones(X_test.shape[0]), X_test]  # Добавляем единичный столбец для тестовых данных.
    y_pred = X @ theta  # Вычисляем предсказания на основе параметров модели.
    print("Анализ завершен.")  # Печатаем сообщение о завершении анализа.
    return y_pred  # Возвращаем предсказания.

# Функция для визуализации результатов
def plot_results(y_test, y_pred):
    print("Построение графика.")  # Печатаем сообщение о начале построения графика.
    plt.figure(figsize=(10, 6))  # Устанавливаем размер графика.
    plt.scatter(range(len(y_test)), y_test, color='blue', label='Фактические значения')  # Строим график фактических значений.
    plt.scatter(range(len(y_pred)), y_pred, color='red', label='Прогнозируемые значения')  # Строим график прогнозируемых значений.
    plt.title('Фактические и прогнозируемые значения')  # Добавляем заголовок.
    plt.xlabel('Индекс')  # Добавляем подпись оси X.
    plt.ylabel('Значение')  # Добавляем подпись оси Y.
    plt.legend()  # Отображаем легенду.
    plt.grid()  # Добавляем сетку на график.
    plt.show()  # Отображаем график.

# Функция для оценки модели
def evaluate_model(y_test, y_pred):
    print("Оценка модели.")  # Печатаем сообщение о начале оценки модели.
    r2 = r2_score(y_test, y_pred)  # Вычисляем коэффициент детерминации (R^2).
    mae = mean_absolute_error(y_test, y_pred)  # Вычисляем среднюю абсолютную ошибку (MAE).
    print(f"Оценка завершена. R^2: {r2}, MAE: {mae}")  # Печатаем результаты оценки.

# Функция для создания и сохранения графа DAG с помощью Graphviz
def draw_dag_graph():
    dot = Digraph(comment='DAG: Метод наименьших квадратов с датасетом Wine', format='png')  # Создаем объект для графа.
    dot.attr(fontname='Arial', fontsize='12')  # Устанавливаем шрифт и размер текста для узлов графа.

    # Определяем узлы (шаги DAG)
    dot.node('A', 'Загрузка данных', style='filled', fillcolor='#FFCC80', shape='box', fontsize='10')  # Узел для загрузки данных.
    dot.node('B', 'Нормализация данных', style='filled', fillcolor='#90CAF9', shape='box', fontsize='10')  # Узел для нормализации данных.
    dot.node('C', 'Разделение данных', style='filled', fillcolor='#A5D6A7', shape='box', fontsize='10')  # Узел для разделения данных.
    dot.node('D', 'Применение МНК', style='filled', fillcolor='#FFAB91', shape='box', fontsize='10')  # Узел для применения МНК.
    dot.node('E', 'Анализ результатов', style='filled', fillcolor='#FFCC80', shape='box', fontsize='10')  # Узел для анализа результатов.
    dot.node('F', 'Визуализация результатов', style='filled', fillcolor='#80CBC4', shape='box', fontsize='10')  # Узел для визуализации результатов.
    dot.node('G', 'Оценка модели', style='filled', fillcolor='#FFAB91', shape='box', fontsize='10')  # Узел для оценки модели.

    # Определяем зависимости между узлами
    dot.edge('A', 'B', label='1')  # Загрузка данных -> Нормализация данных.
    dot.edge('B', 'C', label='2')  # Нормализация данных -> Разделение данных.
    dot.edge('C', 'D', label='3')  # Разделение данных -> Применение МНК.
    dot.edge('D', 'E', label='4')  # Применение МНК -> Анализ результатов.
    dot.edge('E', 'F', label='5')  # Анализ результатов -> Визуализация результатов.
    dot.edge('D', 'G', label='6')  # Применение МНК -> Оценка модели.

    # Сохраняем граф как изображение
    output_path = '/content/dag_wine_least_squares_workflow'  # Указываем путь для сохранения графа.
    dot.render(output_path, cleanup=True)  # Генерируем и сохраняем граф.
    print(f"Граф DAG сохранен как '{output_path}.png'")  # Печатаем сообщение о сохранении графа.

# Вызов функции для рисования графа
draw_dag_graph()  # Генерируем и сохраняем граф.

# Проверка наличия файла
file_path = '/content/dag_wine_least_squares_workflow.png'  # Указываем путь к сохраненному файлу.
if os.path.exists(file_path):  # Проверяем, существует ли файл.
    print("Файл найден:", file_path)  # Печатаем сообщение, если файл найден.
else:
    print("Файл не найден.")  # Печатаем сообщение, если файл не найден.

# Отображение графа
from IPython.display import Image  # Импортируем функцию для отображения изображений в Jupyter.
Image(file_path)  # Отображаем изображение графа.

# Вызов всех функций для выполнения
data, target = load_data()  # Загружаем данные.
data_normalized = normalize_data(data)  # Нормализуем данные.
X_train, X_test, y_train, y_test = split_data(data_normalized, target)  # Разделяем данные на обучающие и тестовые выборки.
theta = apply_least_squares(X_train, y_train)  # Применяем метод наименьших квадратов.
y_pred = analyze_results(X_test, y_test, theta)  # Анализируем результаты.
plot_results(y_test, y_pred)  # Строим график результатов.
evaluate_model(y_test, y_pred)  # Оцениваем модель.
