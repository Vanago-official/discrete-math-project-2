
# Код згенеровано за допомогою ШІ (ChatGPT)

def algorithm(graph):
    n = len(graph)
    reach = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach
