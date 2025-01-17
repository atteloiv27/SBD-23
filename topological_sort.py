from collections import deque

def topological_sort(graph): # позволяет упорядочить процессы в порядке их исполнения 
    # на основе матрицы конфликтов
    # graph: словарь вида {узел: [соседние узлы]}
    in_degree = {node: 0 for node in graph}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            in_degree[neighbor] += 1
    
    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) != len(graph):
        raise ValueError("Граф содержит цикл!")
    
    return result

# Пример использования
graph = {
    'A': ['B'],
    'B': ['D', 'C'],
    'C': [],
    'D': []
}

order = topological_sort(graph)
print(order)  # Выведет: ['A', 'B', 'C', 'D']
