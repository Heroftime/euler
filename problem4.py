"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindromes = []
for n in range(100, 1000):
    for i in range(100, 1000):
        prod = n * i

        if str(prod) == str(prod)[::-1]:
            palindromes.append(prod)

print(max(palindromes))
