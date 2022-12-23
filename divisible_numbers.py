
#Write a program that asks the user to enter a number and prints out all the divisors of that number.

number= int(input("Enter a number: "))
for i in range(1,number+1):
    if(number%i==0):
        print(i)