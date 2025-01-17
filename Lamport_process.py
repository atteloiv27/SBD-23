import threading
import random

class LamportClock:
    def __init__(self):
        self.clock = 0  # Инициализация логического времени для процесса, начинаем с 0.

    def get_time(self):
        return self.clock  # Возвращает текущее логическое время процесса.

    def increment(self):
        self.clock += 1  # Увеличивает логическое время на 1 (текущее событие).

    def update(self, other_clock):
        self.clock = max(self.clock, other_clock)  # Обновляет локальное время на максимум между текущим и временем другого процесса.
        
class Process:
    def __init__(self, id):
        self.id = id  # Присваиваем уникальный идентификатор процессу.
        self.clock = LamportClock()  # Инициализация объекта LamportClock для отслеживания времени.
        self.messages_sent = []  # Список для хранения отправленных сообщений.
        self.messages_recieved = []  # Список для хранения полученных сообщений.
        self.lock = threading.Lock()  # Блокировка для синхронизации доступа к данным (предотвращает гонки).

    def send_message(self, recipient, event_type="message"):
        with self.lock:  # Блокируем текущий процесс для предотвращения гонки потоков.
            self.clock.increment()  # Увеличиваем логическое время при отправке сообщения.
            message = (event_type, self.id, self.clock.get_time())  # Формируем сообщение, содержащее тип события, id и логическое время.
            self.messages_sent.append(message)  # Добавляем сообщение в список отправленных сообщений.
            recipient.receive_message(message)  # Отправляем сообщение получателю, вызывая его метод receive_message.

    def receive_message(self, message):
        with self.lock:  # Блокируем процесс для безопасного доступа к данным.
            event_type, sender_id, sender_clock = message  # Извлекаем тип события, id отправителя и логическое время отправителя.
            self.clock.update(sender_clock)  # Обновляем наше время, используя максимальное из локального времени и времени отправителя.
            self.messages_recieved.append(message)  # Добавляем сообщение в список полученных сообщений.

    def run(self):
        for _ in range(3):  # Каждый процесс выполняет цикл из 3 шагов, отправляя сообщения.
            recipients = list(filter(lambda p: p.id != self.id, processes))  # Составляем список всех процессов, кроме самого себя.
            if recipients:
                recipient = recipients[random.randint(0, len(recipients)-1)]  # Выбираем случайного получателя.
                self.send_message(recipient)  # Отправляем сообщение выбранному получателю.
                
# Создаем список процессов, каждый процесс получает уникальный идентификатор (id).
processes = [Process(id=i) for i in range(3)]  # В данном случае создаются три процесса с id 0, 1, 2.

# Создаем и запускаем потоки для каждого процесса, чтобы они могли работать параллельно.
threads = [threading.Thread(target=p.run) for p in processes]  # Для каждого процесса создаем поток.
for t in threads:
    t.start()  # Запускаем каждый поток.

# Выводим результаты после выполнения всех потоков.
for p in processes:
    print(f"Процесс {p.id}:")  # Для каждого процесса выводим его id.
    print("\tОтправленные сообщения:", p.messages_sent)  # Выводим все отправленные сообщения этого процесса.
    print("\tПолученные сообщения:", p.messages_recieved)  # Выводим все полученные сообщения этого процесса.
