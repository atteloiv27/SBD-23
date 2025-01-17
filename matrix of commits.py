import numpy as np  # Импортируем библиотеку NumPy для работы с массивами и матрицами.

a = np.zeros((5,5))  # Создаем матрицу смежности размером 5x5, заполненную нулями.

a[0, 1] = 1
a[0, 3] = 1
a[0, 4] = 1  # Коммитет 0 не может проходить одновременно с 1, 3, 4
a[2, 1] = 1
a[2, 3] = 1  # Коммитет 2 не может проходить одновременно с 1, 3
a[4, 3] = 1  # Коммитет 4 не может проходить одновременно с 3

print("Матрица смежности:", a, sep="\n")

b = np.zeros(5)  # Создаем массив b размером 5, заполненный нулями.
print("Первоначальный массив b:", b)

print("Сумма по столбцам a:", a.sum(axis=0))
print("Сумма по строкам a:", a.sum(axis=1))

first_step = np.where(a.sum(axis=0) == 0)[0]  # Находим столбцы, которые равны 0
print("Первый шаг - коммитеты без зависимостей:", first_step)

b[first_step] = 1  # Отмечаем их как выполненные в массиве b
print("Массив b после первого шага:", b)

completed = set(first_step)  # Множество завершенных коммитетов
steps = [first_step]  # Будет храниться последовательность шагов выполнения коммитетов

def find_next_step(completed, a):
    next_step = []
    for i in range(a.shape[0]):  # Цикл по количеству строк = кол-во коммитетов
        if i not in completed:
            # Проверяем, что все зависимости этого коммитета выполнены
            # т.е. что зависимость не существует или уже выполнена
            if all(a[i, j] == 0 or j in completed for j in range(a.shape[1])):
                next_step.append(i)
    return next_step

while len(completed) < a.shape[0]:  # Пока не все коммитеты завершены
    next_step = find_next_step(completed, a)
    if not next_step:
        break
    
    steps.append(next_step)
    completed.update(next_step) 
    b[next_step] = 1  # Отмечаем коммитеты как выполненные
    print(f"Массив b на шаге {len(steps)}:", b)
    print(f"Шаг {len(steps)}: Коммитеты {next_step}")

print("\nИтоговая последовательность выполнения:")
for i, step in enumerate(steps):
    print(f"Шаг {i+1}: Коммитеты {step}")
