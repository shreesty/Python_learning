'''
Write a program that asks the user for two numbers and prints Close if the numbers are
within .001 of each other and Not close otherwise.
'''

number1=float(input("Enter first number: "))
number2=float(input("Enter another number: "))

if(abs(number1-number2)<0.001):
    print("Close")
else:
    print("Not Close")