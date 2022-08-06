def nearest_value(values: set, one: int) -> int:
    # your code here
    values = sorted(values)
    old = values[0]
    # Проверяем, находится ли число в списке. Если да, возвращаем его.
    if one in values:
        return one
    # Проверяем, если первое значение списка больше, чем число, то возвращаем это первое значение.
    elif old > one:
        return old
    # Проверяем, если последнее значение списка меньше, чем число, то возвращаем это последнее значение.
    elif one > values[-1]:
        return values[-1]
    # Иначе, пробегаем по всем элементам списка и ищем два числа из списка.
    # Одно число меньше числа из условия, второе - больше числа из условия.
    # Берем то число, у которого меньше разница с числом из условия.
    # Если разница одинакова, то возвращается наименьшее число из найденных.
    else:
        for now in values:
            if old < one < now:
                a = one - old
                b = now - one
                first = old
                break
            old = now
        return now if a > b else first


if __name__ == "__main__":
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
