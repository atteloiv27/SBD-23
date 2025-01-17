def dfs(matrix, start, visited, component):
    visited[start] = True  # Помечаем вершину start как посещенную
    component.append(start)  # Добавляем вершину start в текущую компоненту
    n = len(matrix)  # Получаем количество вершин (размер матрицы смежности)
    for neighbor in range(n):  # Проходим по всем соседям вершины start
        if matrix[start][neighbor] == 1 and not visited[neighbor]:  # Если есть ребро и сосед не посещен
            dfs(matrix, neighbor, visited, component)  # Рекурсивно вызываем dfs для соседа

def find_connected_components(matrix):
    n = len(matrix)  # Получаем количество вершин
    components = []  # Список для хранения всех компонент связности
    visited = [False] * n  # Список для отслеживания посещенных вершин, изначально все непосещены
    
    for vertex in range(n):  # Проходим по всем вершинам
        if not visited[vertex]:  # Если вершина еще не была посещена
            component = []  # Начинаем новую компоненту связности
            dfs(matrix, vertex, visited, component)  # Запускаем dfs для этой вершины
            components.append(component)  # Добавляем найденную компоненту в общий список
    
    return components  # Возвращаем список всех компонент связности

# Пример использования
matrix = [
    [0, 1, 1, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0]
]

components = find_connected_components(matrix)
print(components)

