# compute_factorials.py

import sys
import math
from joblib import load, dump, Parallel, delayed

# Увеличиваем лимит на количество цифр в больших числах (например, до 10 млн).
# Это нужно сделать как можно раньше.
sys.set_int_max_str_digits(10_000_000)

def compute_sum_of_factorials(prime_list):
    """Считает сумму факториалов из списка простых чисел."""
    return sum(math.factorial(p) for p in prime_list)

if __name__ == "__main__":
    primes_1000 = load("primes_dump.joblib")

    n_chunks = 10
    n_jobs = 4
    chunk_size = len(primes_1000) // n_chunks

    chunks = [primes_1000[i:i+chunk_size] for i in range(0, len(primes_1000), chunk_size)]

    partial_sums = Parallel(n_jobs=n_jobs)(
        delayed(compute_sum_of_factorials)(chunk)
        for chunk in chunks
    )

    total_sum = sum(partial_sums)

    dump(total_sum, "factorials_sum.joblib")
    print("Сумма факториалов 1000 простых чисел > 1000:", total_sum)
