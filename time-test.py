import time
import statistics

# тут потрібно імпортувати graph_generator та graph_algorythm


# початкові значення для тесту
vertices = 10 # вершини (20-200)
density = 50 # щільність (10-50)
num_iter = 0 # кількість ітерацій для тесту

times = [] # список для результатів

# тест алгоритму
for i in range(num_iter):
    #graph = graph_generator(vertices, density)

    start_time = time.perf_counter() # початок заміру

    # тут виклик функції алгоритму

    end_time = time.perf_counter() # кінець заміру

    clean_time = end_time - start_time
    times.append(clean_time)


if times:
    avg_time = statistics.mean(times)

    # Стандартне відхилення - показує, наскільки сильно відрізнялися результати між собою (дисперсія)
    stdev = statistics.stdev(times)

    print("-" * 50)
    print(f"Результати тесту на {num_iter} ітерацій:")
    print(f"Середній час {avg_time * 1000:.6f} мс")
    print(f"Максимальний час: {max(times) * 1000:.6f} мс")
    print(f"Мінімальний час: {min(times) * 1000:.6f} мс")
    print(f"Стандартне відхилення: {stdev * 1000:.6f} мс")
else:
    print("Не вдалося зібрати дані вимірювань.")