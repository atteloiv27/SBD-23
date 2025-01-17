import time  # Импортируем модуль time, который предоставляет функции для работы с временем.
import requests  # Импортируем библиотеку requests для отправки HTTP-запросов.

def read_example() -> None:
    response = requests.get('https://www.example.com')  # Отправляем GET-запрос на сайт https://www.example.com.
    print(response.status_code)  # Печатаем статусный код ответа, например 200, если запрос успешен.

sync_start = time.time()  # Засекаем время начала выполнения синхронного кода.
read_example()  # Выполняем первый запрос и ожидаем его завершения.
read_example()  # Выполняем второй запрос, но программа будет ждать, пока не завершится первый.
sync_end = time.time()  # Засекаем время после выполнения обоих запросов.
print(f'Синхронное выполнение заняло {sync_end - sync_start:.4f} с.')  # Выводим время выполнения.
