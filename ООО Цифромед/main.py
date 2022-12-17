import random
from test_1 import solve

for _ in range(10):
    my_list = list(set(random.randint(1, 100) for _ in range(10)))
    a, b = random.randint(0, len(my_list) - 1), random.randint(0, len(my_list) - 1)
    target = my_list[a] + my_list[b]

    print(*my_list)
    print(f'num_1 = {a}, num_2 = {b}')
    print(f'{my_list[a]} + {my_list[b]} = {target}')
    print(solve(my_list, target))
