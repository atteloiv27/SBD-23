import asyncio  # Импортируем библиотеку asyncio для асинхронного выполнения задач.

async def delay(delay_second: int) -> int:
    # какой тип переменной возвращает функция, лучше всегда указывать
    print(f'засыпаю на {delay_second} секунд')  # Выводим сообщение о начале задержки.
    await asyncio.sleep(delay_second)  # Асинхронно засыпаем на delay_second секунд.
    print(f'сон в течение {delay_second} cек закончился')  # Выводим сообщение о завершении задержки.
    return delay_second  # Возвращаем значение задержки (delay_second).

async def main():
    sleep_for_three = asyncio.create_task(delay(3))  # Создаем задачу для выполнения функции delay(3).
    print(type(sleep_for_three))  # Выводим тип объекта, который возвращает create_task.
    result = await sleep_for_three  # Ждем завершения задачи sleep_for_three.
    print(result)  # Выводим результат, возвращенный функцией delay(3).

asyncio.run(main())  # Запускаем асинхронную функцию main и блокируем выполнение до ее завершения.
