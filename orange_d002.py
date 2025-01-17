import joblib  # Импортируем библиотеку joblib для загрузки и сохранения данных.
import sys  # Импортируем sys для работы с системными параметрами, хотя в этом коде не используется.
import click  # Импортируем click для создания интерфейса командной строки.

@click.command()  # Декоратор, который превращает функцию в команду для командной строки.
@click.option("--infile", default="df1.job", prompt="df1.job", help="Входной файл.")  
@click.option("--outfile", default="df2.job", prompt="df2.job", help="Выходной файл.")

def run(infile, outfile):  # Основная функция, которая выполняет обработку данных.
    """Очищает выборку от NaN"""  # Докстринг, описывающий задачу.
    df = joblib.load(infile)  # Загружаем DataFrame из файла infile.

    df = df.dropna()  # Удаляем все строки с пропущенными значениями (NaN) из DataFrame.

    joblib.dump(df, outfile)  # Сохраняем очищенный DataFrame в файл outfile.

    click.echo(f"Создан файл: {outfile}!")  # Выводим сообщение о том, что файл был успешно создан.

if __name__ == '__main__':  # Проверка, если файл запускается как основной.
    run()  # Запуск основной функции run().
