def solve(dict_status):
    start, end = 0, len(dict_status) - 1
    while abs(start - end) > 1:
        mid = (start + end) // 2
        if dict_status[mid]:
            start = mid + 1
        else:
            end = mid
    if dict_status[start]:
        return f'Первая сломанная версия: {end}.'
    else:
        return f'Первая сломанная версия: {start}.'
