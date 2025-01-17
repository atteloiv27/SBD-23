import time  # Импортируем модуль time для измерения времени выполнения.
import tracemalloc  # Импортируем модуль tracemalloc для отслеживания использования памяти.
from multiprocessing import Pool  # Импортируем Pool из multiprocessing для параллельного выполнения процессов.

def check_combination(args):
    D, O, DONALD, GERALD, ROBERT = args  # Распаковываем аргументы в переменные D, O, DONALD, GERALD, ROBERT
    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D)
    digits_zero = [i for i in digits if i != 0]  # Без нуля для первых букв слова, так как 6-значные числа
    results = []  # Список для хранения найденных решений
    unique_letters = set(DONALD + GERALD + ROBERT)  # Извлекаем уникальные буквы из слов DONALD, GERALD и ROBERT

    # Проверяем, что количество уникальных букв не превышает 10, иначе нет решения
    if len(unique_letters) > 10:
        return results  # Если больше 10 уникальных букв, сразу возвращаем пустой список (нет решения)

    # Генерация всех возможных комбинаций для оставшихся букв
    for N in digits:  # Перебираем цифры для буквы N
        if N in (D, O):  # Если N уже равно D или O, пропускаем итерацию, так как буквы должны быть уникальными
            continue
        for A in digits:  # Перебираем цифры для буквы A
            if A in (D, O, N):  # Если A уже равно D, O или N, пропускаем итерацию
                continue
            for L in digits:  # Перебираем цифры для буквы L
                if L in (D, O, N, A):  # Если L уже равно D, O, N или A, пропускаем итерацию
                    continue
                for G in digits_zero:  # G не может быть 0 (не может быть первой цифрой числа)
                    if G in (D, O, N, A, L):  # Если G уже равно одной из предыдущих цифр, пропускаем итерацию
                        continue
                    for E in digits:  # Перебираем цифры для буквы E
                        if E in (D, O, N, A, L, G):  # Если E уже равно одной из предыдущих цифр, пропускаем итерацию
                            continue
                        for R in digits_zero:  # R не может быть 0 (не может быть первой цифрой числа)
                            if R in (D, O, N, A, L, G, E):  # Если R уже равно одной из предыдущих цифр, пропускаем итерацию
                                continue
                            for B in digits:  # Перебираем цифры для буквы B
                                if B in (D, O, N, A, L, G, E, R):  # Если B уже равно одной из предыдущих цифр, пропускаем итерацию
                                    continue
                                for T in digits:  # Перебираем цифры для буквы T
                                    if T in (D, O, N, A, L, G, E, R, B):  # Если T уже равно одной из предыдущих цифр, пропускаем итерацию
                                        continue
                                    # Вычисляем значения для DONALD, GERALD и ROBERT, используя текущие цифры
                                    DONALD_value = D * 100000 + O * 10000 + N * 1000 + A * 100 + L * 10 + D
                                    GERALD_value = G * 100000 + E * 10000 + R * 1000 + A * 100 + L * 10 + D
                                    ROBERT_value = R * 100000 + O * 10000 + B * 1000 + E * 100 + R * 10 + T

                                    # Проверяем, выполняется ли уравнение
                                    if DONALD_value + GERALD_value == ROBERT_value:
                                        results.append((DONALD_value, GERALD_value, ROBERT_value, O, G, E, R, B, T, A, L, N))
                                        # Выводим найденное решение
                                        print(f"Решение найдено: DONALD = {DONALD_value}, GERALD = {GERALD_value}, ROBERT = {ROBERT_value}")
                                        print(f"Сопоставление: D={D}, O={O}, N={N}, A={A}, L={L}, G={G}, E={E}, R={R}, B={B}, T={T}")

    return results  # Возвращаем все найденные решения

def solve_ford(DONALD="DONALD", GERALD="GERALD", ROBERT="ROBERT", D=5):  # Задаем слова и фиксированное значение для D
    # Запускаем отслеживание памяти
    tracemalloc.start()  # Начинаем отслеживание использования памяти.

    # Время начала выполнения
    start_time = time.time()  # Записываем текущее время перед запуском процесса.

    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D)

    # Создаем пул процессов для параллельного выполнения
    with Pool(processes=2) as pool:  # Используем 2 процесса для параллельной обработки
        results = pool.map(check_combination, [(D, O, DONALD, GERALD, ROBERT) for O in digits if O != D]) 
        # Для каждого возможного значения O, вызываем check_combination с соответствующими аргументами

    # Записываем время окончания выполнения
    end_time = time.time()  # Получаем текущее время после выполнения.

    # Получаем объем задействованной памяти
    current, peak = tracemalloc.get_traced_memory()  # Получаем текущее и пиковое значение памяти, использованной во время выполнения.

    # Останавливаем отслеживание памяти
    tracemalloc.stop()  # Останавливаем отслеживание использования памяти.

    # Выводим результаты
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")  # Выводим время выполнения
    print(f"Текущий объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковый объем памяти: {peak / (1024 * 1024):.2f} МБ")
    # Выводим текущий и пиковый объем использованной памяти в мегабайтах.

solve_ford()  # Вызываем функцию для решения задачи.
