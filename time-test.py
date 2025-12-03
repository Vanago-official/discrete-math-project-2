import time
import statistics

# тут потрібно імпортувати graph_generator та graph_algorythm

# підготовка csv файлу
with open("result.csv", "w") as f:
    f.write(f"avg,max,min,stdev,vertices,density\n")

# початкові значення для тесту, від якого до якого перевіряти
# вершини (20-200)
ver_min = 20
ver_max = 200
ver_step = 10

# щільність (10-50)
den_min = 10
den_max = 50
den_step = 10

# кількість ітерацій для кожної пари
num_iter = 5

first_iter_cycle = int((ver_max - ver_min) / ver_step)
second_iter_cycle = int((den_max - den_min) / den_step)

# тест алгоритму
f = open("result.csv", "a")

ver = ver_min
den = den_min

for k in range(first_iter_cycle + 1):
    for j in range(second_iter_cycle + 1):
        times = []  # список для результатів
        for i in range(num_iter):
            # graph = graph_generator(ver, den)

            start_time = time.perf_counter()  # початок заміру

            # тут виклик функції алгоритму
            for _ in range(99999):
                _ += 1

            end_time = time.perf_counter()  # кінець заміру

            clean_time = end_time - start_time
            times.append(clean_time)

        if times:
            avg_time = float(f"{statistics.mean(times) * 1000:.6f}")
            max_time = float(f"{max(times) * 1000:.6f}")
            min_time = float(f"{min(times) * 1000:.6f}")
            stdev = float(
                f"{statistics.stdev(times) * 1000:.6f}")  # Стандартне відхилення - показує, наскільки сильно відрізнялися результати між собою (дисперсія)

            f.write(f"{avg_time},{max_time},{min_time},{stdev},{ver},{den}\n")
        else:
            f.write(f"0,0,0,0,0,0\n")

        den += den_step
    ver += ver_step
    den = den_min
f.close()
