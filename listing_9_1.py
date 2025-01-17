from aiohttp import web  # Импортируем модуль web для создания веб-приложений.
from datetime import datetime  # Импортируем класс datetime для работы с датой и временем.
from aiohttp.web_request import Request  # Импортируем тип Request для типизации аргумента в обработчиках.
from aiohttp.web_response import Response  # Импортируем тип Response для типизации возвращаемых значений.

routes = web.RouteTableDef()  # Создаем объект, который будет хранить наши маршруты.

@routes.get('/t')  # Декоратор, который связывает URL-путь '/t' с обработчиком.
async def time(request: Request) -> Response:  # Асинхронная функция-обработчик для пути '/t'.
    today = datetime.today()  # Получаем текущую дату и время.
    for i in range(0, 1000001):  # Имитация работы (задержка).
        pass
    result = {  # Формируем результат для ответа.
        'month': today.month,  # Месяц текущей даты.
        'day': today.day,  # День текущей даты.
        'time': str(today.time()),  # Время текущей даты в строковом формате.
        'message': 'Здравствуй, мир!'  # Приветственное сообщение на русском.
    }
    return web.json_response(result)  # Возвращаем результат в формате JSON.

@routes.get('/time')  # Декоратор, который связывает URL-путь '/time' с обработчиком.
async def time(request: Request) -> Response:  # Асинхронная функция-обработчик для пути '/time'.
    today = datetime.today()  # Получаем текущую дату и время.
    for i in range(0, 1000001):  # Имитация работы (задержка).
        pass
    result = {  # Формируем результат для ответа.
        'month': today.month,  # Месяц текущей даты.
        'day': today.day,  # День текущей даты.
        'time': str(today.time()),  # Время текущей даты в строковом формате.
        'message': 'Hello world!'  # Приветственное сообщение на английском.
    }
    return web.json_response(result)  # Возвращаем результат в формате JSON.

app = web.Application()  # Создаем объект приложения.
app.add_routes(routes)  # Добавляем маршруты в приложение.
web.run_app(app)  # Запускаем приложение на сервере.
