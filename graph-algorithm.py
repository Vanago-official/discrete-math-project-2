# тут ти повинен написати код алгоритму Уошелла для досяжності матриці
# тут має бути функція def algorithm(graph):
# приймає граф, і повинна повернути граф який пройшов алгоритм уошела, можеш
# згенерувати за допомогою ШІ тільки залишиш коментар що ШІ писав
# потім закомітити й запушити
# я б зробив все сам, але тобі теж треба робота

# Код згенеровано за допомогою ШІ (ChatGPT)

def algorithm(graph):
    n = len(graph)
    reach = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    return reach
#допомога ШІ