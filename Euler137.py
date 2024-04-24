from math import sqrt
from fractions import Fraction

def A_F(x):
    return Fraction(x, 1 - x - x**2)

def F(n):
    phi = (1 + sqrt(5)) / 2
    return round(phi**n / sqrt(5))

for n in range(2, 31, 2):
    x = Fraction(F(n), F(n + 1))
    print(n, x, A_F(x))