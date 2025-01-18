import joblib
from joblib import Parallel, delayed, load

def calculate_sum_of_factorials(primes_path, factorial_func_path):
    # Загрузка данных и функции
    primes = joblib.load(primes_path)
    factorial = joblib.load(factorial_func_path)

    # Вычисление факториалов параллельно
    def compute_factorial(n):
        return factorial(n)

    factorials = Parallel(n_jobs=-1)(delayed(compute_factorial)(n) for n in primes)
    return sum(factorials)

# Этот блок для тестирования, чтобы можно было запустить как отдельный скрипт
if __name__ == "__main__":
    result = calculate_sum_of_factorials("primes.pkl", "factorial_func.pkl")
    print(f"Сумма факториалов: {result}")
