#. Write a program that generates a random number, x, between 1 and 50, a random number y
#between 2 and 5, and computes x^Y.

from random import randint
x=randint(1,50)
print(x)
y=randint(2,5)
print(y)

print("x^y: ",x**y)