#  Write a program that asks the user for their name and how many times to print it. 
# The program should print out the user’s name the specified number of times.

name= input("Enter your name: ")
num= int(input("Enter how many times to print your name: "))

for i in range(1,num+1):
    print(name)
