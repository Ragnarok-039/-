from is_broken_version import broken_version
from test_2 import solve

# ������� ��� ������� 10 ��������� �������.
# for _ in range(10):
test_list = broken_version()
bad_index, dict_status = test_list[1], test_list[0]

print(f'������ ��������� ������: {solve(dict_status)}.')
print(bad_index)
print(dict_status, type(dict_status))
print('-' * 50)
