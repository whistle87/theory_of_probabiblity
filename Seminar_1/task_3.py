"""
В ящике имеется 15 деталей, из которых 9 окрашены.
Рабочий случайным образом извлекает 3 детали.
Какова вероятность того, что все извлеченные детали окрашены?
"""

import math

n = (math.factorial(9) / (math.factorial(3) * math.factorial(9 -3))) * \
    (math.factorial(6) / (math.factorial(0) * math.factorial(6 -0)))
m = math.factorial(15) / (math.factorial(3) * math.factorial(15 - 3))
P_A = n / m
print(P_A)
