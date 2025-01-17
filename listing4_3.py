def frange(start, stop, increment):
  x = start  # Инициализация переменной x значением start
  while x < stop:  # Пока x меньше stop, продолжаем цикл
    yield x  # Возвращаем текущее значение x
    x += increment   # x увеличивается на величину increment

for n in frange(0, 4, 0.5):
  print(n)

list(frange(0, 1, 0.125))

def countdown(n):
  print('Starting to count from', n)
  while n > 0:  # Пока n больше 0, продолжаем цикл
    yield n  # Возвращаем текущее значение n
    n -= 1  # Уменьшаем n на 1
  print('Done!')  # После завершения цикла выводим сообщение

# Создает генератор – обратите внимание на отсутствие вывода
c = countdown(3)
# Выполняется до первого yield и выдает значение
next(c)
# Выполняется до следующего yield
next(c)
# Выполняется до следующего yield
next(c)
 # Выполняется до следующего yield (итерирование останавливается)
next(c)
