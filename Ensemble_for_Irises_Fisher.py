import asyncio  # Импортируем библиотеку для работы с асинхронностью и задачами.
import numpy as np  # Импортируем библиотеку для работы с массивами и случайными числами.
import pandas as pd  # Импортируем библиотеку для работы с данными в табличном виде.
from sklearn.datasets import load_iris  # Импортируем набор данных Ирисы Фишера из sklearn.
from sklearn.model_selection import train_test_split  # Импортируем функцию для разделения данных на обучающие и тестовые выборки.
from sklearn.linear_model import LogisticRegression  # Импортируем модель логистической регрессии.
from sklearn.ensemble import RandomForestClassifier  # Импортируем ансамблевый классификатор (Random Forest).
from sklearn.metrics import accuracy_score, confusion_matrix  # Импортируем метрики для оценки качества модели.
import seaborn as sns  # Импортируем библиотеку для визуализации данных.
import matplotlib.pyplot as plt  # Импортируем библиотеку для создания графиков.
import nest_asyncio  # Импортируем библиотеку, позволяющую использовать асинхронность внутри уже работающего цикла событий.

# Для разрешения вложенного выполнения асинхронных функций
nest_asyncio.apply()  # Эта функция позволяет использовать асинхронность внутри уже работающего цикла событий, необходима для работы с Jupyter или IPython.

# Загружаем датасет Ирисы Фишера
iris = load_iris()  # Загружаем встроенный датасет Ирисы из sklearn.
df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])  # Создаем DataFrame, где храним данные (4 признака).
df['species'] = pd.Categorical.from_codes(iris['target'], iris['target_names'])  # Добавляем столбец 'species' с названиями видов ирисов.

# Рассчитаем среднее и стандартное отклонение для каждого вида ириса
distribution_params = df.groupby('species').agg(['mean', 'std'])  # Группируем по видам и вычисляем для каждого вида средние и стандартные отклонения по признакам.

# sepal length (cm) — длина чашелистика,
# sepal width (cm) — ширина чашелистика,
# petal length (cm) — длина лепестка,
# petal width (cm) — ширина лепестка.

# Переименуем столбцы, чтобы было проще работать
distribution_params.columns = [
    'sepal_length_mean', 'sepal_length_std',  # Среднее и стандартное отклонение для длины чашелистика.
    'sepal_width_mean', 'sepal_width_std',    # Среднее и стандартное отклонение для ширины чашелистика.
    'petal_length_mean', 'petal_length_std',  # Среднее и стандартное отклонение для длины лепестка.
    'petal_width_mean', 'petal_width_std'     # Среднее и стандартное отклонение для ширины лепестка.
]

# Количество новых записей для генерации
num_samples = 10**6  # Мы генерируем 1 миллион образцов для каждой категории.

# Функция для генерации новых образцов, используя среднее и стандартное отклонение
def generate_samples(params, num_samples):
    means = params.filter(like='mean').values  # Извлекаем значения средних из данных.
    stds = params.filter(like='std').values  # Извлекаем значения стандартных отклонений.
    return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))  # Генерируем случайные данные по нормальному распределению.

# Асинхронная функция для вызова generate_samples в отдельном фоновом потоке, не блокируя основной поток выполнения
async def async_generate_samples(params, num_samples):
    return await asyncio.to_thread(generate_samples, params, num_samples)  # Асинхронно вызываем функцию генерации данных в другом потоке.

async def main():
    tasks = []  # Список для хранения асинхронных задач.
    for species, params in distribution_params.iterrows():  # Перебираем все виды ирисов.
        tasks.append(async_generate_samples(params, num_samples))  # Для каждого вида запускаем асинхронную задачу для генерации данных.

    # Ждем завершения всех задач
    results = await asyncio.gather(*tasks)  # Собираем результаты всех асинхронных задач.

    # Генерируем данные для каждого вида ириса и объединяем в один DataFrame
    df_generated = pd.concat(
        [pd.DataFrame(result, columns=iris['feature_names']).assign(species=species) for result, species in zip(results, distribution_params.index)],
        ignore_index=True
    )

    print(f"Размер сгенерированного датафрейма: {df_generated.shape}")  # Выводим размер сгенерированного датафрейма.

    # Преобразуем категорию species в числовой формат (кодируем виды ирисов числами)
    df_generated['species'] = df_generated['species'].astype('category').cat.codes

    # Разделяем данные на признаки (X) и целевую переменную (y)
    X = df_generated.drop('species', axis=1)  # Признаки — все столбцы, кроме 'species'.
    y = df_generated['species']  # Целевая переменная — столбец 'species'.

    # Разделяем данные на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)  # Разделяем данные на 80% для обучения и 20% для тестирования.

    # Модель логистической регрессии
    log_reg = LogisticRegression(max_iter=1000)  # Создаем модель логистической регрессии.
    log_reg.fit(X_train, y_train)  # Обучаем модель на обучающих данных.
    log_reg_predictions = log_reg.predict_proba(X_train)  # Получаем прогнозы вероятностей для обучающих данных.

    # Модель Random Forest
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=1)  # Создаем модель случайного леса с 100 деревьями.
    rf_classifier.fit(log_reg_predictions, y_train)  # Обучаем модель на предсказаниях логистической регрессии.

    log_reg_test_predictions = log_reg.predict_proba(X_test)  # Получаем прогнозы вероятностей для тестовых данных.
    rf_predictions = rf_classifier.predict(log_reg_test_predictions)  # Получаем финальные предсказания с помощью случайного леса.

    # Оценка точности ансамбля
    accuracy = accuracy_score(y_test, rf_predictions)  # Оцениваем точность модели на тестовых данных.
    print(f"Точность ансамбля (логистическая регрессия + Random Forest): {accuracy:.4f}")  # Выводим точность.

    # Матрица ошибок (confusion matrix)
    conf_matrix = confusion_matrix(y_test, rf_predictions)  # Строим матрицу ошибок.

    # Визуализация матрицы ошибок
    plt.figure(figsize=(8, 6))  # Размер фигуры.
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['Setosa', 'Versicolor', 'Virginica'],
                yticklabels=['Setosa', 'Versicolor', 'Virginica'])  # Визуализируем матрицу ошибок с подписями для классов.
    plt.title('Confusion Matrix')  # Заголовок графика.
    plt.xlabel('Predicted')  # Подпись оси X.
    plt.ylabel('Actual')  # Подпись оси Y.
    plt.show()  # Отображаем график.

# Создаем асинхронную функцию для запуска main
async def run():
    await main()  # Запускаем функцию main.

# Запускаем асинхронную функцию
asyncio.run(run())  # Запускаем основной цикл событий, который выполнит run.
