import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(0)  # Устанавливаем начальное значение генератора случайных чисел для воспроизводимости.

df_penguins = sns.load_dataset('penguins')  # Загружаем встроенный датасет о пингвинах из Seaborn.

# species: Вид пингвина (Adelie, Chinstrap, Gentoo).
# island: Остров, на котором был найден пингвин (Torgersen, Dream, или Biscoe).
# bill_length_mm: Длина клюва в миллиметрах.
# bill_depth_mm: Глубина клюва в миллиметрах.
# flipper_length_mm: Длина ласт в миллиметрах.
# body_mass_g: Масса тела в граммах.
# sex: Пол пингвина.

df_penguins = df_penguins.dropna()  # Удаляем строки с пропущенными значениями.

df_penguins['species'] = df_penguins['species'].astype('category').cat.codes  # Преобразуем категориальную переменную 'species' в числовой формат.

numeric_columns = df_penguins.select_dtypes(include=[np.number])  # Оставляем только числовые столбцы для дальнейшей обработки.

numeric_columns['species'] = df_penguins['species']  # Добавляем обратно категорию 'species' для дальнейшего анализа.

distribution_params = numeric_columns.groupby('species').agg(['mean', 'std']).reset_index()  # Рассчитываем среднее и стандартное отклонение для каждого вида.

distribution_params = numeric_columns.groupby('species').agg(['mean', 'std']).reset_index()  # Рассчитываем среднее и стандартное отклонение для каждого вида.

distribution_params.columns = ['species'] + [f'{col}_{stat}' for col, stat in distribution_params.columns[1:]]  # Преобразуем имена столбцов для удобства.

num_samples = 10000  # Количество новых записей для генерации.

def generate_samples(means, stds, num_samples):  # Функция для генерации данных, основанных на нормальном распределении.
    return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))  # Генерация данных на основе нормального распределения.

samples = []  # Список для хранения сгенерированных данных.
species_list = []  # Список для хранения меток вида.
for _, params in distribution_params.iterrows():  # Проходим по строкам DataFrame с параметрами распределений.
    means = params.filter(like='mean').values  # Извлекаем средние значения.
    stds = params.filter(like='std').values  # Извлекаем стандартные отклонения.
    generated_samples = generate_samples(means, stds, num_samples)  # Генерируем выборку.
    samples.append(generated_samples)  # Добавляем сгенерированные данные в список.
    species_list.append(np.full(num_samples, params['species']))  # Добавляем метки видов.

generated_columns = [col for col in distribution_params.columns if '_mean' in col]  # Список названий столбцов для сгенерированных данных.
df_generated = pd.DataFrame(np.vstack(samples), columns=generated_columns)  # Объединяем все сгенерированные данные в один DataFrame.

df_generated['species'] = np.concatenate(species_list)  # Добавляем столбец с метками видов.

df_generated.columns = [col.replace('_mean', '') for col in df_generated.columns]  # Убираем суффикс '_mean' из имен столбцов.

plt.figure(figsize=(10, 6))  # Устанавливаем размер графика.
sns.scatterplot(data=df_penguins, x='bill_length_mm', y='bill_depth_mm', hue='species', palette='deep')  # Строим диаграмму рассеяния.
plt.title('Характеристики пингвинов в зависимости от их вида')  # Заголовок графика.
plt.xlabel('Длина клюва (мм)')  # Метка оси X.
plt.ylabel('Глубина клюва (мм)')  # Метка оси Y.
plt.legend(title='Вид', labels=['Adelie', 'Chinstrap', 'Gentoo'])  # Легенда с названиями видов.
plt.show()  # Отображаем график.

X = df_generated.drop('species', axis=1)  # Отделяем признаки (X) от меток (y).
y = df_generated['species']  # Метки (y) — это столбец 'species'.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)  # Разделяем данные на обучающую и тестовую выборки.

nb_classifier = GaussianNB()  # Инициализируем наивный байесовский классификатор.
nb_classifier.fit(X_train, y_train)  # Обучаем модель на обучающих данных.

nb_predictions = nb_classifier.predict(X_test)  # Получаем предсказания на тестовой выборке.

accuracy = accuracy_score(y_test, nb_predictions)  # Оцениваем точность модели.
print(f"Точность Байесовского классификатора: {accuracy:.4f}")  # Выводим точность модели.

conf_matrix = confusion_matrix(y_test, nb_predictions)  # Строим матрицу ошибок.

plt.figure(figsize=(8, 6))  # Устанавливаем размер графика.
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Adelie', 'Chinstrap', 'Gentoo'],
            yticklabels=['Adelie', 'Chinstrap', 'Gentoo'])  # Строим тепловую карту
