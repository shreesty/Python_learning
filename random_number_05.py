'''
Generate a random number between 1 and 10. Ask the user to guess the number and print a
message based on whether they get it right or not.
'''

num=int(input("Enter a number: "))

from random import randint
number= randint(1,10)
print("Random Number is: ",number)

if(num==number):
    print("User got the number right.")
else:
    print("Wrong guess.")