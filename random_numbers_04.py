'''
Write a program that generates 50 random numbers such that the first number is between 1
and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
1 and 51.
'''

from random import randint     # Generate 50 random numbers

for i in range(1,51):
    numbers=randint(1,i+1)    # Generate a random number between 1 and i+2
    print(numbers)
