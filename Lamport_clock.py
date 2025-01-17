class LamportClock:
    def __init__(self):
        self.clock = 0  # Инициализация логического времени с нуля. Каждому процессу будет присвоено начальное время 0.

    def get_time(self):
        return self.clock  # Метод возвращает текущее значение логического времени процесса.

    def increment(self):
        self.clock += 1  # Увеличиваем логическое время на 1. Это событие внутри процесса.

    def update(self, other_clock):
        self.clock = max(self.clock, other_clock)  # Метод для синхронизации: обновляем локальное время на максимальное значение
        # между текущим временем и временем, полученным от другого процесса.

# Пример использования
node_a = LamportClock()  # Создание первого объекта LamportClock (процесс A).
node_b = LamportClock()  # Создание второго объекта LamportClock (процесс B).

print("Initial time for node A:", node_a.get_time())  # Печатаем начальное время для процесса A (должно быть 0).
print("Initial time for node B:", node_b.get_time())  # Печатаем начальное время для процесса B (должно быть 0).

# Node A increments its clock
node_a.increment()  # Процесс A увеличивает свое логическое время на 1.
node_a.increment()  # Процесс A увеличивает свое логическое время на 1 снова.
node_a.increment()  # Процесс A увеличивает свое логическое время на 1 в третий раз.
print("Node A increments its clock to:", node_a.get_time())  # Печатаем текущее время процесса A (должно быть 3).

# Node B sends a message with timestamp 2 to Node A
message_timestamp = 2  # Пример временной метки, которую процесс B отправляет процессу A (время равно 2).

node_a.update(message_timestamp)  # Процесс A обновляет свое время на максимум между текущим временем и временем,
# которое он получил от процесса B (в данном случае, max(3, 2)).
print("Node A updates its clock after receiving message from Node B:", node_a.get_time())  # Печатаем новое время процесса A (должно остаться 3, так как оно уже больше времени процесса B).
