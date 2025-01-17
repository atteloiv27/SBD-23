import asyncio  # Импортируем библиотеку asyncio для работы с асинхронным кодом.

async def delay(delay_second: int) -> int:
    # какой тип переменной возвращает функция, лучше всегда указывать
    print(f'засыпаю на {delay_second} секунд')  # Выводим сообщение о начале задержки.
    await asyncio.sleep(delay_second)  # Асинхронно засыпаем на delay_second секунд.
    print(f'сон в течение {delay_second} cек закончился')  # Выводим сообщение о завершении задержки.
    return delay_second  # Возвращаем значение задержки (delay_second).

async def add_one(number: int) -> int:
    return number + 1  # Увеличиваем переданное число на 1 и возвращаем результат.

async def hello_world_message() -> str:
    await delay(1)  # Вызов асинхронной функции delay на 1 секунду.
    return 'Hello World!'  # Возвращаем строку 'Hello World!'

async def main() -> None:
    message = await hello_world_message()  # Ждем результат от функции hello_world_message.
    one_plus_one = await add_one(1)  # Ждем результат от функции add_one.
    print(one_plus_one)  # Выводим результат add_one, который равен 2.
    print(message)  # Выводим строку 'Hello World!', возвращенную функцией hello_world_message.

asyncio.run(main())  # Запускаем асинхронную функцию main и блокируем выполнение до ее завершения.
