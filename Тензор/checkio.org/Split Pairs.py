def split_pairs(a):
    # your code here
    need_list = []
    start, end = 0, 2
    while start < len(a):
        now = a[start:end]
        need_list.append(now)
        start += 2
        end += 2
    if len(a) % 2 == 0:
        return need_list
    else:
        return need_list[:-1] + [need_list[-1] + "_"]


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
