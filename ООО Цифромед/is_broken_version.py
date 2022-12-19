# Функция для генерации словаря версий.


def broken_version():
    import random

    version_dict = {}
    # Берем случайный индекс, с которого пойду сломанные версии.
    bad_index = random.randint(0, 9)

    # Формируем словарь из 10 элементов.
    # Все элементы левее bad_index - True.
    # Соответственно, все элементы, начиная с bad_index до конца словаря - False.
    for i in range(10):
        version_dict.setdefault(i, True if i < bad_index else False)

    # Возвращает словарь и первый сломанный индекс.
    return version_dict, bad_index
