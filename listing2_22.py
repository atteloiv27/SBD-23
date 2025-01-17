import asyncio  # Импортируем библиотеку asyncio для работы с асинхронным кодом.

def call_later():
    print("Меня вызовут в ближайшем будущем!")  # Простая функция, которая выводит сообщение.

async def delay(delay_second: int) -> int:
    # async нужен, потому что task относится к библиотеке async
    # какой тип переменной возвращает функция, лучше всегда указывать
    print(f'засыпаю на {delay_second} секунд')  # Выводим сообщение, что функция начнет засыпать.
    await asyncio.sleep(delay_second)  # Асинхронно засыпаем на delay_second секунд.
    print(f'сон в течение {delay_second} cек закончился')  # После того, как функция "просыпается", выводим сообщение.
    return delay_second  # Возвращаем переданное количество секунд.

async def main():
    loop = asyncio.get_running_loop()  # Получаем текущий активный событийный цикл.
    loop.call_soon(call_later)  # Регистируем функцию call_later, чтобы она была вызвана как можно скорее.
    await delay(1)  # Выполняем функцию delay с задержкой на 1 секунду.

asyncio.run(main(), debug=True)  # Запускаем асинхронную функцию main() и включаем режим отладки.
