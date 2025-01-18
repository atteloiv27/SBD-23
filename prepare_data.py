# prepare_data.py

from joblib import dump
import math

def is_prime(n: int) -> bool:
    """Проверка, является ли число простым."""
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    # Проверяем делители до корня из n
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def get_primes_greater_than_1000(limit_count: int = 1000):
    """Находит 'limit_count' простых чисел, которые строго больше 1000."""
    primes = []
    num = 1001
    while len(primes) < limit_count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def factorial(n: int) -> int:
    """Вычисление факториала числа n (при желании можно заменить на math.factorial)."""
    # Можно просто return math.factorial(n), но для примера реализуем вручную
    if n < 2:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

if __name__ == "__main__":
    # Шаг 1: Получаем 1000 простых чисел > 1000
    primes_1000 = get_primes_greater_than_1000(limit_count=1000)
    
    # Опционально можно сохранить и функцию factorial, но обычно достаточно списка простых чисел
    # Если действительно нужно, можно сериализовать объект, содержащий обе функции/данные,
    # но обычно передают только данные.
    
    # Шаг 2: Сериализуем список простых чисел в файл
    dump(primes_1000, "primes_dump.joblib")
    
    print("Простые числа сохранены в primes_dump.joblib")
