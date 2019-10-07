"""Ratio multiplier without classes"""
from math import gcd

ratio_pairs = [
    ((1, 1), (2, 7)),
    ((4, 12), (8, 19)),
    ((10, 2), (4, 17))
]

def multiply_ratios(ratio1, ratio2):
    antecedent = ratio1[0] * ratio2[0]
    consequent = ratio1[1] * ratio2[1]
    divisor = gcd(antecedent, consequent)
    return(antecedent//divisor, consequent//divisor)

for r1, r2 in ratio_pairs:
    product = multiply_ratios(r1, r2)
    print(f'The product of {r1[0]}:{r1[1]} and {r2[0]}:{r2[1]} is {product[0]}:{product[1]}')
