import sys
import joblib
import numpy as np
from sympy import primerange
import script2  # импортируем второй скрипт

sys.set_int_max_str_digits(10_000_000)

# Генерация 1000 простых чисел больше 1000
primes = list(primerange(1001, 15000))[:1000]

# Определение функции факториала
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Сохранение данных и функции для передачи
joblib.dump(primes, "primes.pkl")
joblib.dump(factorial, "factorial_func.pkl")

# Вызов второго скрипта
result = script2.calculate_sum_of_factorials("primes.pkl", "factorial_func.pkl")

print(f"Сумма факториалов: {result}")