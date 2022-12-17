import random

my_list = [random.randint(1, 100) for _ in range(10)]
a, b = 2, 6
target = my_list[a] + my_list[b]
flag = True

print(my_list)
print(target)

for i in range(len(my_list)):
    if flag:
        a = my_list[i]
        for j in range(len(my_list)):
            b = my_list[j]
            if i != j and a + b == target:
                print(i, j)
                flag = False
                break
