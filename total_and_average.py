'''

Write a program that asks the user to enter three numbers (use three separate input statements). 
Create variables called total and average that hold the sum and average of the three numbers and 
print out the values of total and average.

'''

number1=int(input("Enter 1st number: "))
number2=int(input("Enter 2nd number: "))
number3=int(input("Enter 3rd number: "))

total= number1+ number2 + number3
print("Sum of the three numbers is: ",total)

average= (total/3)
print("Average of the three numbers is: ",average)