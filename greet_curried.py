def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)  # Формирует строку приветствия и выводит на экран.
    return greet  # Возвращаем функцию greet, которая использует переменную greeting.

def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)  # Формирует строку приветствия и выводит на экран.
    return greet  # Возвращаем функцию greet, которая использует переменную greeting.

greet_hello('German')  # Выводит "Hello, German"
greet_hello('Ivan')    # Выводит "Hello, Ivan"

xxx = dict()  # Создаем пустой словарь
greet_curried('Hi')('Roma')  # Приветствует "Hi, Roma"

xxx["Hello"] = greet_curried('Hello')  # Приветствие для "Hello"
xxx["Hi"] = greet_curried('Hi')        # Приветствие для "Hi"
xxx["Привет"] = greet_curried('Привет')  # Приветствие для "Привет"

xxx["Привет"]("Roma")  # Выводит "Привет, Roma"
xxx["Hi"]("Roma")      # Выводит "Hi, Roma"
