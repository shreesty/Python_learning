# Write a program that generates a random number between 1 and 10 and prints your name that many times.


name=input("Enter your name: ")
from random import randint
num= randint(1,10)
print("Random number is : ",num)
for i in range(num):
    print("Name: ",name)
