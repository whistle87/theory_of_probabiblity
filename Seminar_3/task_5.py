"""
Устройство состоит из трех деталей.
Для первой детали вероятность выйти из строя в первый месяц равна 0.1,
для второй - 0.2, для третьей - 0.25.
Какова вероятность того, что в первый месяц выйдут из строя:
а). все детали б). только две детали в). хотя бы одна деталь г). от одной до двух деталей?
"""

# выйдут из строя все детали
P_all = 0.1 * 0.2 * 0.25
# только две детали. Значит выйдут из строя 1 и 2, а 3 нет, или 2 и 3, а 1 нет, или 1 и 3, а 2 нет.
# Сумма вероятностей этих событий - общая вероятность, что выйдут из строя две детали
P_1_and_2 = 0.1 * 0.2 * 0.75
P_1_and_3 = 0.1 * 0.8 * 0.25
P_2_and_3 = 0.9 * 0.2 * 0.25
P_2 = P_1_and_3 + P_1_and_2 + P_2_and_3
# хотя бы одна деталь
P_1_or_more = 1 - (0.9 * 0.8 * 0.75)
# от одной до двух деталей
P_1 = 0.1 * 0.8 * 0.75 + 0.9 * 0.2 * 0.75 + 0.9 * 0.8 * 0.25
P_1_or_2 = P_1 + P_2
print(f"Вероятность, что из строя выйдут \nа) все детали {P_all}\nб) только две детали {P_2}\n"
      f"в)хотя бы одна деталь {P_1_or_more},\nг)от одной до двух деталей {P_1_or_2}")
