import joblib  # Импортируем библиотеку joblib для загрузки и сохранения данных.
import click  # Импортируем библиотеку click для создания интерфейса командной строки.
import numpy as np  # Импортируем numpy для работы с массивами и числовыми операциями.
import pandas as pd  # Импортируем pandas для обработки данных в виде DataFrame.

@click.command()  # Декоратор, который превращает функцию в команду для командной строки.
@click.option("--infile", default="df2.job", prompt="df2.job", help="Входной файл.")  
@click.option("--outfile", default="df3.job", prompt="df3.job", help="Выходной файл.")  

def run(infile, outfile):  # Основная функция, которая выполняет обработку данных.
    """ Увеличиваем размер выборки"""  # Докстринг, описывающий задачу.
    df = joblib.load(infile)  # Загружаем DataFrame из файла infile.
    df['species'] = df['species'].astype('category').cat.codes  # Преобразуем столбец 'species' в числовые коды категорий.
    numeric_columns = df.select_dtypes(include=[np.number])  # Отбираем только числовые столбцы для дальнейшей агрегации.
    numeric_columns['species'] = df['species']  # Добавляем столбец 'species' обратно в числовые столбцы.
    distribution_params = numeric_columns.groupby('species').agg(['mean', 'std']).reset_index()  
    distribution_params.columns = ['species'] + [f'{col}_{stat}' for col, stat in distribution_params.columns[1:]]  
    num_samples = 10000  # Устанавливаем количество новых записей, которые нужно сгенерировать.
  
    def generate_samples(means, stds, num_samples):  # Определяем функцию для генерации новых данных.
        return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))  
      
    samples = []  # Список для хранения сгенерированных данных.
    species_list = []  # Список для хранения меток классов (видов).
    for _, params in distribution_params.iterrows():  # Для каждой строки в distribution_params (для каждого вида).
        means = params.filter(like='mean').values  # Извлекаем средние значения.
        stds = params.filter(like='std').values  # Извлекаем стандартные отклонения.
        generated_samples = generate_samples(means, stds, num_samples)  # Генерируем образцы.
        samples.append(generated_samples)  # Добавляем сгенерированные образцы в список.
        species_list.append(np.full(num_samples, params['species']))  # Добавляем метки вида в список.

    generated_columns = [col for col in distribution_params.columns if '_mean' in col]  # Имена столбцов для новых данных.
    df_generated = pd.DataFrame(np.vstack(samples), columns=generated_columns)  # Объединяем данные и создаем DataFrame.

    df_generated['species'] = np.concatenate(species_list)  # Добавляем столбец с метками видов.

    df_generated.columns = [col.replace('_mean', '') for col in df_generated.columns]  # Убираем суффикс '_mean' из имен столбцов.

    joblib.dump(df_generated, outfile)  # Сохраняем сгенерированные данные в файл outfile.
    click.echo(f"Создан файл: {outfile}!")  # Выводим сообщение о создании выходного файла.

if __name__ == '__main__':  # Проверка, если файл запускается как основной.
    run()  # Запуск основной функции run().

