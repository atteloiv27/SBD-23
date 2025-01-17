import numpy as np  # Импортируем библиотеку numpy для работы с массивами и матрицами
from multiprocessing import Pool  # Импортируем Pool из библиотеки multiprocessing для параллельного выполнения процессов

def calculate_row_sum(matrix, row_index): # Вычисляет сумму элементов одной строки матрицы
    return matrix[row_index].sum()  # Возвращает сумму элементов в строке с индексом row_index
  
def calculate_col_sum(matrix, col_index): # Вычисляет сумму элементов одного столбца матрицы
    return matrix[:, col_index].sum()  # Возвращает сумму элементов в столбце с индексом col_index

matrix = np.random.randint(0, 10, size=(1000, 1000))  # Генерируем случайную матрицу размером 1000x1000 с целыми числами от 0 до 9
print(matrix.shape[0])  # Печатаем количество строк в матрице (1000)

with Pool(processes=4) as pool:  # Создаем пул из 4 процессов
    row_sums = pool.starmap(calculate_row_sum, ((matrix, i) for i in range(matrix.shape[0]))) 
    # Параллельно вычисляем суммы строк, передавая каждому процессу индекс строки

with Pool(processes=4) as pool:  # Создаем пул из 4 процессов
    col_sums = pool.starmap(calculate_col_sum, ((matrix, i) for i in range(matrix.shape[1]))) 
    # Параллельно вычисляем суммы столбцов, передавая каждому процессу индекс столбца

print("Суммы строк:", row_sums[:5])  # Показываем первые 5 сумм строк
print("Суммы столбцов:", col_sums[:5])  # Показываем первые 5 сумм столбцов
