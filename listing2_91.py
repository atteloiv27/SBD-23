import asyncio  # Импортируем библиотеку asyncio, которая используется для написания асинхронного кода на Python.

async def delay(delay_second: int) -> int:
    # async нужен, потому что task относится к библиотеке async
    # какой тип переменной возвращает функция, лучше всегда указывать
    print(f'засыпаю на {delay_second} секунд')  # Печатаем, что начинается задержка на указанное количество секунд.
    await asyncio.sleep(delay_second)  # Асинхронно "засыпаем" на указанный период времени.
    print(f'сон в течение {delay_second} cек закончился')  # Печатаем, что задержка завершена.
    return delay_second  # Возвращаем количество секунд, на которые произошла задержка.

async def main():
    tasks = []  # Создаем пустой список для хранения задач.
    for _ in range(10):  # Создаем 10 задач, можно 1000, но выводить много будет.
        task = asyncio.create_task(delay(3))  # Создаем асинхронную задачу, которая выполнит функцию delay(3).
        tasks.append(task)  # Добавляем задачу в список tasks.

  
    await asyncio.gather(*tasks)  # Дожидаемся завершения всех созданных задач, переданных в gather.

asyncio.run(main())  # Запускаем асинхронную функцию main, используя asyncio.run().

async def main():
    xs = [asyncio.create_task(delay(x)) for x in range(10)]  # Создаем список задач для задержек от 0 до 9 секунд.
    for x in xs:
        await x  # Для каждой задачи ожидаем завершения.

asyncio.run(main())  # Запускаем асинхронную функцию main, используя asyncio.run().

