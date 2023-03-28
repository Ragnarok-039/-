# Задача 2.
# Функция для поиска двух индексов списка, дающих в сумме число == target.
# Индексы имеют порядок согласно логике python (нумерация начинается с 0, а не с 1).
def two_sum(nums, target):
    for i in range(len(nums)):
        a = nums[i]
        for j in range(len(nums)):
            b = nums[j]
            # Возвращаем два индекса только в том случае, если сумма значений списка по этим индексам == target и
            # индекс 1 != индекс 2.
            if i != j and a + b == target:
                return [i, j]


numbers = [2, 7, 11, 15]
target = 9
print(two_sum(numbers, target))
