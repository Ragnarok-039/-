import random
from test_1 import solve

for _ in range(10):
    my_list = list(set(random.randint(1, 100) for _ in range(10)))
    a, b = random.randint(0, len(my_list) - 1), random.randint(0, len(my_list) - 1)
    target = my_list[a] + my_list[b]

    print(f'Список чисел: {my_list}')
    print(f'Случайный индекс 1: {a}, Случайный индекс 2: {b}')
    print(f'{my_list[a]} + {my_list[b]} = {target}')
    print(f'Найденные с помощью функции индексы: {solve(my_list, target)}')
    print('-' * 50)
