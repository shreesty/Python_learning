'''
Write a program that asks the user to enter a number and prints the sum of the divisors of
that number. 
'''
sum=0
num=int(input("Enter a number: "))
for i in range(1, num+1):
    if(num%i==0):
        print(i)
        sum=sum+i
print("Sum of the divisors is: ",sum)       