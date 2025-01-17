from multiprocessing import Pool  # Импортируем Pool для параллельной обработки с использованием нескольких процессов
import functools  # Импортируем functools для использования reduce, который позволяет объединить результаты

def mapper(text): # Функция mapper разбивает текст на слова и возвращает пары (слово, 1)
    words = text.split()  # Разбиваем текст на отдельные слова по пробелам.
    return [(word.lower(), 1) for word in words]  # Возвращаем список кортежей (слово, 1) для каждого слова

def reducer(key_value_pairs): # Функция reducer суммирует количество одинаковых слов
    key, values = key_value_pairs  # Распаковываем кортеж (ключ, значения) в переменные
    return key, sum(values)  # Суммируем все значения для одного ключа (слова) и возвращаем результат

# Пример текста
texts = [
    "Привет мир",
    "Добро пожаловать в мир параллельных вычислений",
    "Мир - это наше общее пространство"
]
print(mapper(texts[0]))  # Первая строка

# Используем пул процессов для параллельной обработки
with Pool(processes=4) as pool:
    # Этап map
    intermediate_results = pool.map(mapper, texts)
    print(intermediate_results)

# Объединяем результаты от разных процессов
flattened_intermediate_results = functools.reduce(lambda x, y: x + y, intermediate_results)
print(flattened_intermediate_results)

# Этап reduce
final_result = {}  # Создаем пустой словарь для хранения окончательных результатов.
for pair in flattened_intermediate_results:
    if pair[0] not in final_result:  # Если слово еще не добавлено в словарь
        final_result[pair[0]] = pair[1]  # Добавляем пару (слово, 1)
    else:
        final_result[pair[0]] += pair[1]  # Если слово уже есть в словаре, увеличиваем его счетчик.

# Сортируем словарь по количеству слов
sorted_final_result = dict(sorted(final_result.items(), key=lambda item: item[1], reverse=True))

# Выводим результат
for word, count in sorted_final_result.items():
    print(f"{word}: {count}")


