import pandas
import matplotlib.pyplot

# Було використано Gemini
def visualize_results(filename="result.csv"):

    # Зчитування даних
    try:
        df = pandas.read_csv(filename)
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено. Переконайтеся, що ви запустили тест.")
        return
    except Exception as e:
        print(f"Помилка при зчитуванні файлу: {e}")
        return

    # Отримання унікальних значень щільності для різних ліній на графіку
    unique_densities = df['density'].unique()

    # Графік
    matplotlib.pyplot.figure(figsize=(10, 6))

    for den in unique_densities:

        subset = df[df['density'] == den]

        # Побудова графіка.
        matplotlib.pyplot.plot(
            subset['vertices'],
            subset['avg'],
            label=f'Щільність {den}%',
            marker='o',  # Круглі маркери для точок даних
            linestyle='-'
        )

    matplotlib.pyplot.title('Залежність середнього часу виконання від розміру графа (N)', fontsize=14)
    matplotlib.pyplot.xlabel('Кількість вершин (N)', fontsize=12)
    matplotlib.pyplot.ylabel('Середній час виконання (мс)', fontsize=12)
    matplotlib.pyplot.legend(title="Щільність графа")
    matplotlib.pyplot.grid(True, linestyle='--', alpha=0.7)  # Легка сітка
    matplotlib.pyplot.show()


visualize_results("Graphs/result.csv")