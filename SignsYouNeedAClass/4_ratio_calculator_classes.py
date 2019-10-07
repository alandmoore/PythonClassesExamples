"""Ratio multiplier with classes"""
from math import gcd

class Ratio:

    def __init__(self, antecedent, consequent):
        self.antecedent = antecedent
        self.consequent = consequent

    def __mul__(self, other):
        ant = self.antecedent * other.antecedent
        con = self.consequent * other.consequent
        divisor = gcd(ant, con)
        return Ratio(ant//divisor, con//divisor)

    def __str__(self):
        return f'{self.antecedent}:{self.consequent}'

ratio_pairs = [
    (Ratio(1, 1), Ratio(2, 7)),
    (Ratio(4, 12), Ratio(8, 19)),
    (Ratio(10, 2), Ratio(4, 17))
]

for r1, r2 in ratio_pairs:
    product = r1 * r2
    print(f'The product of {r1} and {r2} is {product}')
