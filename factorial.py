
'''
Write a program that asks the user for a number and prints out the factorial of that number.
'''
num=int(input("Enter the number: "))

factorial=1
for i in range(1,num+1):
    factorial=factorial * i
print("Factorial of the number is: ",factorial)
