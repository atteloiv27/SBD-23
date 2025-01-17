import asyncio  # Импортируем библиотеку asyncio для асинхронного выполнения задач.

async def delay(delay_second: int) -> int:
    # какой тип переменной возвращает функция, лучше всегда указывать
    print(f'засыпаю на {delay_second} секунд')  # Выводим сообщение, что начинаем задержку на указанное количество секунд.
    await asyncio.sleep(delay_second)  # Асинхронно засыпаем на delay_second секунд.
    print(f'сон в течение {delay_second} cек закончился')  # Выводим сообщение, что задержка завершена.
    return delay_second  # Возвращаем количество секунд, которое было указано для задержки.

async def main():
    sleep_for_three = asyncio.create_task(delay(10))  # Создаем задачу для выполнения функции delay(10).
    sleep_again = asyncio.create_task(delay(3))  # Создаем задачу для выполнения функции delay(3).
    sleep_once_more = asyncio.create_task(delay(8))  # Создаем задачу для выполнения функции delay(8).
    await sleep_for_three  # Ждем завершения первой задачи (задержка 10 секунд).
    await sleep_again  # Ждем завершения второй задачи (задержка 3 секунды).
    await sleep_once_more  # Ждем завершения третьей задачи (задержка 8 секунд).

asyncio.run(main())  # Запускаем асинхронную функцию main и блокируем выполнение до ее завершения.
