import asyncio  # Импортируем библиотеку asyncio для работы с асинхронными задачами.
import aiohttp  # Импортируем библиотеку aiohttp для работы с HTTP-запросами асинхронно.
from aiohttp import ClientSession  # Импортируем класс ClientSession из aiohttp для работы с HTTP-сессиями.
from util import async_timed  # Импортируем декоратор async_timed (предположительно, из внешнего модуля util) для измерения времени выполнения асинхронных функций.

@async_timed()  # Декоратор async_timed применяется к функции, чтобы измерять время её выполнения.
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:  # Асинхронно выполняем GET-запрос по указанному URL.
        return result.status  # Возвращаем статус-код ответа.

@async_timed()  # Декоратор async_timed применяется и к основной функции.
async def main():
    async with aiohttp.ClientSession() as session:  # Создаем асинхронную сессию с aiohttp.
        url = 'https://www.example.com'  # Задаем URL для GET-запроса.
        status = await fetch_status(session, url)  # Выполняем асинхронный запрос и ожидаем результат.
        print(f'Состояние для {url} было равно {status}')  # Печатаем статус HTTP-ответа.

asyncio.run(main())  # Запускаем асинхронную функцию main, которая выполняет основной процесс программы.
