from is_broken_version import broken_version
from test_2 import solve

test_list = broken_version()
bad_index, dict_status = test_list[1], test_list[0]

print(solve(dict_status))
print(bad_index)
print(dict_status, type(dict_status))

# https://blog.skillfactory.ru/glossary/binarnyj-poisk/
