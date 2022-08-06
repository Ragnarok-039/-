def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    # Определить наиболее встречающуюся строку в последовательности.
    my_d = {}
    for now in data:
        # Метод get - возвращает значение ключа, но если его нет, не бросает исключение,
        # а возвращает новую пару ключ: значение (значение - 0).
        # При нахождении ключа увеличивает значение на + 1.
        my_d[now] = my_d.get(now, 0) + 1
    return max(my_d, key=my_d.get)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print('Example:')
    print(most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]))

    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')
