# ������� ��� ��������� ������� ������.


def broken_version():
    import random

    version_dict = {}
    # ����� ��������� ������, � �������� ����� ��������� ������.
    bad_index = random.randint(0, 9)

    # ��������� ������� �� 10 ���������.
    # ��� �������� ����� bad_index - True.
    # ��������������, ��� ��������, ������� � bad_index �� ����� ������� - False.
    for i in range(10):
        version_dict.setdefault(i, True if i < bad_index else False)

    # ���������� ������� � ������ ��������� ������.
    return version_dict, bad_index
