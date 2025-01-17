import time  # Импортируем модуль для измерения времени выполнения.
import tracemalloc  # Импортируем модуль для отслеживания использования памяти.
from joblib import Parallel, delayed  # Импортируем Parallel и delayed из библиотеки joblib для параллельных вычислений.

def check_combination(D, O, DONALD, GERALD, ROBERT):
    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D)
    digits_zero = [i for i in digits if i != 0]  # Без нуля для первых букв слова, так как 6-значные числа.
    results = []  # Список для хранения найденных решений.
    unique_letters = set(DONALD + GERALD + ROBERT)  # Извлекаем уникальные буквы из слов DONALD, GERALD и ROBERT.

    # Проверяем, что количество уникальных букв не превышает 10, иначе нет решения.
    if len(unique_letters) > 10:
        return results  # Если более 10 уникальных букв, сразу возвращаем пустой список (нет решения).

    # Генерация всех возможных комбинаций для оставшихся букв.
    for N in digits:  # Перебираем цифры для буквы N.
        if N in (D, O):  # Если N уже равно D или O, пропускаем итерацию, так как буквы должны быть уникальными.
            continue
        for A in digits:  # Перебираем цифры для буквы A.
            if A in (D, O, N):  # Если A уже равно D, O или N, пропускаем итерацию.
                continue
            for L in digits:  # Перебираем цифры для буквы L.
                if L in (D, O, N, A):  # Если L уже равно D, O, N или A, пропускаем итерацию.
                    continue
                for G in digits_zero:  # G не может быть 0 (не может быть первой цифрой числа).
                    if G in (D, O, N, A, L):  # Если G уже равно одной из предыдущих цифр, пропускаем итерацию.
                        continue
                    for E in digits:  # Перебираем цифры для буквы E.
                        if E in (D, O, N, A, L, G):  # Если E уже равно одной из предыдущих цифр, пропускаем итерацию.
                            continue
                        for R in digits_zero:  # R не может быть 0 (не может быть первой цифрой числа).
                            if R in (D, O, N, A, L, G, E):  # Если R уже равно одной из предыдущих цифр, пропускаем итерацию.
                                continue
                            for B in digits:  # Перебираем цифры для буквы B.
                                if B in (D, O, N, A, L, G, E, R):  # Если B уже равно одной из предыдущих цифр, пропускаем итерацию.
                                    continue
                                for T in digits:  # Перебираем цифры для буквы T.
                                    if T in (D, O, N, A, L, G, E, R, B):  # Если T уже равно одной из предыдущих цифр, пропускаем итерацию.
                                        continue
                                    # Вычисляем значения для DONALD, GERALD и ROBERT, используя текущие цифры.
                                    DONALD_value = D * 100000 + O * 10000 + N * 1000 + A * 100 + L * 10 + D
                                    GERALD_value = G * 100000 + E * 10000 + R * 1000 + A * 100 + L * 10 + D
                                    ROBERT_value = R * 100000 + O * 10000 + B * 1000 + E * 100 + R * 10 + T

                                    # Проверяем, выполняется ли уравнение.
                                    if DONALD_value + GERALD_value == ROBERT_value:
                                        results.append((DONALD_value, GERALD_value, ROBERT_value, O, G, E, R, B, T, A, L, N))
                                        # Выводим найденное решение.
                                        print(f"Решение найдено: DONALD = {DONALD_value}, GERALD = {GERALD_value}, ROBERT = {ROBERT_value}")
                                        print(f"Сопоставление: D={D}, O={O}, N={N}, A={A}, L={L}, G={G}, E={E}, R={R}, B={B}, T={T}")

    return results  # Возвращаем все найденные решения.

def solve_ford(DONALD="DONALD", GERALD="GERALD", ROBERT="ROBERT", D=5):  # Задаем слова и фиксированное значение для D.
    # Запускаем отслеживание памяти.
    tracemalloc.start()

    # Время начала выполнения.
    start_time = time.time()

    digits = [i for i in range(10) if i != D]  # Доступные цифры (0-9 без D).
    
    # Параллельное выполнение с использованием библиотеки joblib.
    Parallel(n_jobs=2)(delayed(check_combination)(D, O, DONALD, GERALD, ROBERT) for O in digits if O != D)
    # Параллельно выполняем check_combination для каждого возможного значения O, исключая D.
    # В параметре `n_jobs=2` указываем, что хотим использовать 2 параллельных процесса.

    # Записываем время окончания выполнения.
    end_time = time.time()

    # Получаем объем задействованной памяти.
    current, peak = tracemalloc.get_traced_memory()

    # Останавливаем отслеживание памяти.
    tracemalloc.stop()
    
    # Выводим результаты.
    print(f"Время выполнения: {end_time - start_time:.2f} секунд")
    print(f"Текущий объем памяти: {current / (1024 * 1024):.2f} МБ; Пиковый объем памяти: {peak / (1024 * 1024):.2f} МБ")

solve_ford()  # Вызываем функцию для решения задачи.
