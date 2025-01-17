import time  # Импортируем модуль time для работы со временем (например, для задержки).
import multiprocessing  # Импортируем модуль multiprocessing для работы с многозадачностью.
import os  # Импортируем модуль os для работы с операционной системой (например, получения идентификатора процесса).
import datetime  # Импортируем модуль datetime для работы с датами и временем.

# Функция, которая будет выполняться в дочернем процессе 01
def hello_from_process01():
    print(f'Привет от дочернего процесса 01 {os.getpid()}!')  # Печатаем идентификатор текущего процесса (PID).
    time.sleep(3)  # Приостанавливаем выполнение на 3 секунды.
    for i in range(100000):  # Процесс выполняет некоторые вычисления.
        2 + 2  # Пример вычислений, на самом деле это не имеет смысла, но занимает некоторое время.

# Функция, которая будет выполняться в дочернем процессе 02
def hello_from_process02():
    print(f'Привет от дочернего процесса 02 {os.getpid()}!')  # Печатаем идентификатор текущего процесса (PID).
    time.sleep(5)  # Приостанавливаем выполнение на 5 секунд.
    for i in range(100000):  # Процесс выполняет некоторые вычисления.
        2 + 2  # Пример вычислений, которые не имеют смысла, но занимают некоторое время.

# Засекаем время начала выполнения программы
start = datetime.datetime.now()

if __name__ == '__main__':  # Убедитесь, что код выполняется только в главном процессе, а не при импорте.
    # Создаем и запускаем несколько дочерних процессов с функциями hello_from_process01 и hello_from_process02.
    hello_process01 = multiprocessing.Process(target=hello_from_process01)  # Создаем процесс для hello_from_process01.
    hello_process01.start()  # Запускаем процесс.

    # Создаем и запускаем 10 дочерних процессов для hello_from_process02.
    hello_process02 = multiprocessing.Process(target=hello_from_process02)
    hello_process02.start()  # Запускаем процесс.

    hello_process03 = multiprocessing.Process(target=hello_from_process02)
    hello_process03.start()  # Запускаем процесс.

    hello_process04 = multiprocessing.Process(target=hello_from_process02)
    hello_process04.start()  # Запускаем процесс.

    hello_process05 = multiprocessing.Process(target=hello_from_process02)
    hello_process05.start()  # Запускаем процесс.

    hello_process06 = multiprocessing.Process(target=hello_from_process02)
    hello_process06.start()  # Запускаем процесс.

    hello_process07 = multiprocessing.Process(target=hello_from_process02)
    hello_process07.start()  # Запускаем процесс.

    hello_process08 = multiprocessing.Process(target=hello_from_process02)
    hello_process08.start()  # Запускаем процесс.

    hello_process09 = multiprocessing.Process(target=hello_from_process02)
    hello_process09.start()  # Запускаем процесс.

    hello_process010 = multiprocessing.Process(target=hello_from_process02)
    hello_process010.start()  # Запускаем процесс.

    hello_process011 = multiprocessing.Process(target=hello_from_process02)
    hello_process011.start()  # Запускаем процесс.

    print(f'Привет от родительского процесса {os.getpid()}')  # Печатаем идентификатор родительского процесса.

    # Ожидаем завершения всех дочерних процессов с помощью метода join().
    hello_process01.join()
    hello_process02.join()
    hello_process03.join()
    hello_process04.join()
    hello_process05.join()
    hello_process06.join()
    hello_process07.join()
    hello_process08.join()
    hello_process09.join()
    hello_process010.join()
    hello_process011.join()

# Засекаем время окончания выполнения программы
finish = datetime.datetime.now()

# Выводим разницу во времени между началом и концом выполнения программы.
print(finish - start)
