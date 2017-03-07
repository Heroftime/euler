"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


flag = True
i = 1
sm_number = 0
while flag:
    divis = []
    for n in range(2, 21):
        if i % 5 != 0:
            break

        if i % n == 0:
            divis.append(i)
        else:
            break

    if len(divis) == 19:
        sm_number = i
        flag = False
        break

    #print(i)

    i = i + 1

print(sm_number)
