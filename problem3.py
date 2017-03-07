"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

# Number to find the largest prime factor for
number = 600851475143

factors = []
prime = 1
flag = True
while flag:
    if (number / prime).is_integer():
        factors.append(prime)

    factors_mult = 1
    for fac in factors:
        factors_mult = fac * factors_mult

    if factors_mult == number:
        flag = False

    prime = prime + 1

# Print the largest prime factor
print(max(factors))
