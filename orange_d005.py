import joblib  # Импортируем библиотеку joblib для сериализации (сохранения и загрузки) объектов, таких как модели машинного обучения.
import sys  # Импортируем модуль sys для работы с параметрами командной строки (хотя он не используется в этом коде).
import click  # Импортируем библиотеку click для создания командной строки с параметрами.
import matplotlib.pyplot as plt  # Импортируем библиотеку matplotlib для визуализации данных (построение графиков).
import seaborn as sns  # Импортируем библиотеку seaborn для создания красивых визуализаций данных, особенно тепловых карт.
from sklearn.naive_bayes import GaussianNB  # Импортируем класс GaussianNB для создания Байесовского классификатора на основе нормального распределения.
from sklearn.model_selection import train_test_split  # Импортируем функцию для разделения данных на обучающую и тестовую выборки.
from sklearn.metrics import accuracy_score, confusion_matrix  # Импортируем функции для оценки модели: точность и матрица ошибок.

@click.command()  # Декоратор, который превращает функцию в команду CLI (командную строку) с параметрами.

# @click.option() — указывает, что функция ожидает параметр. В данном случае, два параметра: infile и outfile
@click.option("--infile", default="df4.job", prompt="df4.job", help="Входной файл.")  # Параметр входного файла.
@click.option("--outfile", default="df5.job", prompt="df5.job", help="Выходной файл.")  # Параметр выходного файла.

def run(infile, outfile):  # Определяем основную функцию, которая будет выполнять работу.
    df = joblib.load(infile)  # Загружаем данные из входного файла с помощью joblib.
    X = df.drop('species', axis=1)  # Извлекаем все столбцы, кроме 'species' (функции признаков).
    y = df['species']  # Извлекаем столбец 'species' как целевую переменную (класс).
  
# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

nb_classifier = GaussianNB()  # Создаем объект Байесовского классификатора.
nb_classifier.fit(X_train, y_train)  # Обучаем классификатор на обучающих данных.

nb_predictions = nb_classifier.predict(X_test)  # Используем обученный классификатор для предсказания классов на тестовой выборке.
accuracy = accuracy_score(y_test, nb_predictions)  # Оценка точности предсказаний.
print(f"Точность Байесовского классификатора: {accuracy:.4f}")  # Вывод точности.
conf_matrix = confusion_matrix(y_test, nb_predictions)  # Вычисляем матрицу ошибок.

plt.figure(figsize=(8, 6))  # Настройка размера графика.
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Adelie', 'Chinstrap', 'Gentoo'],
            yticklabels=['Adelie', 'Chinstrap', 'Gentoo'])  # Строим тепловую карту для матрицы ошибок.
plt.title('Матрица ошибок (Confusion Matrix)')  # Заголовок графика.
plt.xlabel('Предсказано')  # Подпись для оси X.
plt.ylabel('Фактическое')  # Подпись для оси Y.
plt.show()  # Отображаем график.

joblib.dump(nb_predictions, outfile)  # Сохраняем предсказания в файл.
click.echo(f"Создан файл: {outfile}!")  # Выводим сообщение о создании выходного файла.

if __name__ == '__main__':  # Проверка, если файл запускается как основной.
    run()  # Запуск функции run, которая выполняет все шаги.

