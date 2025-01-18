import sys
from joblib import dump
import numpy as np
from sympy import primerange
import script2  # импортируем второй скрипт

# Увеличиваем лимит на количество цифр в больших числах (из-за того что в питоне есть ограничение на количество символов в числе, то чтобы вывести сумму мы делаем это)
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
joblib.dump(factorial.__code__, "factorial_func_code.joblib")  # Сериализуем код функции, а не саму функцию

# Вызов второго скрипта
result = script2.calculate_sum_of_factorials("primes.joblib", "factorial_func.joblib")

print(f"Сумма факториалов: {result}")
