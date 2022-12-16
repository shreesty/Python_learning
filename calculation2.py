
#Write a program that asks the user to enter two numbers, x and y, and computes |x−y|/x+y..

x=int(input("Enter 1st number: "))
y=int(input("Enter 2nd number: "))

s=x-y
a= x+y
if(s<0):
    print(-(s)/a)
else:
    print(s/a)