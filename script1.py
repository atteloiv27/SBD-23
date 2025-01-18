import sys
from joblib import dump
import numpy as np
from sympy import primerange
import script2  # импортируем второй скрипт
import inspect

# Увеличиваем лимит на количество цифр в больших числах
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
dump(factorial, "factorial_func.joblib")
dump(primes, "primes.joblib")

# Вызов второго скрипта
result = script2.calculate_sum_of_factorials("primes.joblib", "factorial_func.joblib")

print(f"Сумма факториалов: {result}")
