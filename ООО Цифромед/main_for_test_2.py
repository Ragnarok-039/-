# coding: utf-8
from is_broken_version import broken_version
from test_2 import solve

# Возьмем для примера 10 случайных событий.
for _ in range(10):
    # Формируем словарь с версиями.
    test_list = broken_version()
    # Берем случайно выбранный bad_index и словарь с версиями с помощью функции broken_version().
    bad_index, dict_status = test_list[1], test_list[0]

    print(f'Изначально взятый bad_index: {bad_index}.')
    print(f'Словарь с версиями: {dict_status}', type(dict_status))
    print(f'Найденная с помощью функции первая сломанная версия: {solve(dict_status)}.')
    print('-' * 50)
