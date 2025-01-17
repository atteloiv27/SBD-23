import pandas as pd  # Импортируем библиотеку pandas, которая используется для работы с данными в виде таблиц (DataFrame).
from dash import Dash, dcc, html  # Импортируем необходимые компоненты для создания веб-приложения с использованием Dash.
import plotly.express as px  # Импортируем библиотеку Plotly Express для создания графиков и визуализаций.

# Создание Dash-приложения
app = Dash(__name__)  # Создаем экземпляр приложения Dash. __name__ позволяет Dash определить, какое имя присвоить серверу.

data = {
    "train": ([[2, 2, 1], [1, 1, 1], [1, 1, 2], [1, 2, 2]], ["b", "a", "a", "b"]),
    "test": ([[1, 2, 2]], ['b'])
}

# Создание DataFrame
def create_dataframe(data, label, set_name):
    df = pd.DataFrame(data, columns=["Feature 1", "Feature 2", "Feature 3"])  # Преобразуем данные в DataFrame с именами столбцов.
    df['Prediction'] = label  # Добавляем столбец 'Prediction' для меток (предсказаний).
    df['Set'] = set_name  # Добавляем столбец 'Set' для метки типа выборки ('Train' или 'Test').
    return df  # Возвращаем созданный DataFrame.

# Создание DataFrame для тренировочной и контрольной выборок
df_train = create_dataframe(*data["train"], 'Train')  # Создаем DataFrame для тренировочной выборки.
df_test = create_dataframe(*data["test"], 'Test')  # Создаем DataFrame для тестовой выборки.

# Объединяем обе выборки
df = pd.concat([df_train, df_test], ignore_index=True)  # Объединяем тренировочную и тестовую выборки в один DataFrame.

# Создание 3D графика
fig = px.scatter_3d(df, x="Feature 1", y="Feature 2", z="Feature 3", color="Prediction",
                    title="График предсказаний модели в 3D",
                    labels={"Feature 1": "Признак 1", "Feature 2": "Признак 2", "Feature 3": "Признак 3"},
                    color_discrete_map={"a": "blue", "b": "red"})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash for RandomForestClassifier'),  # Заголовок H1 для приложения.
    dcc.Graph(id='example-graph', figure=fig)  # Вставляем график в приложение Dash с помощью компонента dcc.Graph.
])

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение с включенным режимом отладки (debug).
