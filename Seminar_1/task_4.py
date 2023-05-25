"""
В лотерее 100 билетов. Из них 2 выигрышных.
Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?
"""
import math

n = (math.factorial(2) / (math.factorial(2) * math.factorial(2 - 2))) * \
    (math.factorial(98) / (math.factorial(0) * math.factorial(98 -0)))
m = math.factorial(100) / (math.factorial(2) * math.factorial(100 - 2))
P_A = n / m
print(P_A)
