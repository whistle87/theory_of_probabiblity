"""
1. Из колоды в 52 карты извлекаются случайным образом 4 карты.
a) Найти вероятность того, что все карты – крести.
б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
"""
import math

"""a"""
n = (math.factorial(13) / (math.factorial(4) * math.factorial(13 - 4))) * \
    (math.factorial(39) / (math.factorial(0) * math.factorial(39)))
m = math.factorial(52) / (math.factorial(4) * math.factorial(52 - 4))
P_A = n / m
print(P_A)

"""b"""
n = (math.factorial(4) / (math.factorial(1) * math.factorial(4 - 1)) *
     math.factorial(48) / (math.factorial(3) * math.factorial(48 - 3)) +
     math.factorial(4) / (math.factorial(2) * math.factorial(4 - 2)) *
     math.factorial(48) / (math.factorial(2) * math.factorial(48 - 2)) +
     math.factorial(4) / (math.factorial(3) * math.factorial(4 - 1)) *
     math.factorial(48) / (math.factorial(1) * math.factorial(48 - 1)) +
     math.factorial(4) / (math.factorial(4) * math.factorial(4 - 4)) *
     math.factorial(48) / (math.factorial(0) * math.factorial(48 - 0))) / \
    (math.factorial(52) / (math.factorial(4) * math.factorial(52 - 4)))

P_B = n / m
print(P_B)
