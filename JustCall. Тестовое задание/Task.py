import matplotlib.pyplot as plt
import numpy as np


zone = dict()
count = 0

# Произвел открытие файла.
with open("test.csv", encoding="utf-8") as my_file:
    for line in my_file:
        # Убрал со строк ненужные символы в начале и конце, разделил строку по ",".
        line = line.strip().split(",")
        # Этот блок добавил с целью убрать заголовок таблицы. Счетчик добавил больше для проверки себя.
        if line[2].isalpha():
            count += 1
            continue
        # Из строки выбираю округ, попутно удаляя ненужные символы.
        county = line[0].strip().split("_")
        county = " ".join(county)
        # Создаю словарь из пар: округ и список со всеми значениями длительности звонков.
        if county in zone:
            zone[county].append(float(line[1]))
        else:
            zone[county] = [float(line[1])]

for now in zone:
    # Вычисляю среднее время для каждого округа.
    my_mean = round(np.mean(zone[now]), 3)
    # Вычисляю медианное время для каждого округа.
    my_median = round(np.median(zone[now]), 3)
    # Печатаю вычисленные значения, дополнительно переводя в привычный формат времени "мин сек".
    print(f"Округ: {now}; среднее время: {my_mean}, что составляет: {my_mean // 1} мин {round(my_mean % 1 * 60, 2)} сек;"
          f" медианное время: {my_median}, что составляет: {my_median // 1} мин {round(my_median % 1 * 60, 2)} сек.")
    # Строю гистограмму по выбранному округу.
    # С целью минимизировать воздействие выбросов на график, ограничил его диапазоном от 0 до 3 мин.
    plt.hist(zone[now], bins=100, range={0, 3})
    plt.title(now)
    plt.show()
    # Дополнительно построил ящик с усами с целью показать не только медианные значения, но и первый и третий квартиль.
    plt.boxplot(zone[now], showfliers=False)
    plt.title(now)
    plt.show()
