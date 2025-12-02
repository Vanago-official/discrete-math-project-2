import timeit

# для коректного запуску тесту timeit
setup_code = """
import random
from __main__ import graph_generator
"""

time = timeit.timeit(
    stmt="graph_generator(100, 50)",  # код який тестується
    setup=setup_code,
    number=50  # кількість ітерацій
)

print(time)
