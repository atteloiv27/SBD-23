x = 1
processes = [x for x in range(3)]
print(processes)  # Выведет: [0, 1, 2]

print([x for x in filter(lambda p: p!=2, processes)])  # Выведет: [0, 1]
