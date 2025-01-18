from joblib import dump
import math
import inspect

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0 and n != 2:
        return False
    limit = int(n**0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def get_primes_greater_than_1000(limit_count: int = 1000):
    primes = []
    num = 1001
    while len(primes) < limit_count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def factorial(n: int) -> int:
    if n < 2:
        return 1
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

if __name__ == "__main__":
    primes_1000 = get_primes_greater_than_1000(limit_count=1000)
    
    # Получаем исходный код функции factorial
    factorial_code = inspect.getsource(factorial)
    
    # Упаковываем данные
    data_to_save = {
        "primes": primes_1000,
        "factorial_code": factorial_code
    }

    # Сохраняем в файл
    dump(data_to_save, "primes_and_factorial.joblib")
    
    print("Простые числа и код функции factorial сохранены в primes_and_factorial.joblib")
