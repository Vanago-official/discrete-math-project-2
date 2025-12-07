import random


def graph_generator(vertices: int, density: int) -> list:
    """
    vertices - вершини графа,
    density - щільність графа (0-100),
    """

    # створення пустого графа
    matrix = [[0] * vertices for _ in range(vertices)]

    # заповнення графа
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and random.randint(1, 100) <= density:
                matrix[i][j] = 1
    return matrix
