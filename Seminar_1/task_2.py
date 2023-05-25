"""
На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
Код содержит три цифры, которые нужно нажать одновременно. Какова вероятность того, что человек,
не знающий код, откроет дверь с первой попытки?
"""
import math

n = (math.factorial(3) / (math.factorial(3) * math.factorial(0))) * \
    (math.factorial(7) / (math.factorial(0) * math.factorial(7 -0)))
m = math.factorial(10) / (math.factorial(3) * math.factorial(10 - 3))
P_A = n / m
print(P_A)
