import sys
from joblib import load, dump, Parallel, delayed

# Загружаем данные
data = load("primes_and_factorial.joblib")

# Извлекаем список простых чисел
prime_list = data["primes"]

# Извлекаем код функции factorial
factorial_code = data["factorial_code"]

# Увеличиваем лимит на количество цифр в больших числах (из-за того что в питоне есть ограничение на количество символов в числе, то чтобы вывести сумму мы делаем это)
sys.set_int_max_str_digits(10_000_000)

# Выполняем код функции, чтобы она стала доступной
exec(factorial_code)

def compute_sum_of_factorials(prime_list):
    # Считает сумму факториалов из списка простых чисел
    return sum(factorial(p) for p in prime_list)

if __name__ == "__main__":
    # Параметры для параллельного вычисления
    n_chunks = 10
    n_jobs = 4
    chunk_size = len(prime_list) // n_chunks

    chunks = [prime_list[i:i + chunk_size] for i in range(0, len(prime_list), chunk_size)]

    # Вычисление суммы факториалов параллельно
    partial_sums = Parallel(n_jobs=n_jobs)(
        delayed(compute_sum_of_factorials)(chunk)
        for chunk in chunks
    )

    # Суммируем частичные суммы
    total_sum = sum(partial_sums)

    # Сохраняем результат
    dump(total_sum, "factorials_sum.joblib")
    print("Сумма факториалов 1000 простых чисел > 1000:", total_sum)
