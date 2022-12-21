'''
Write a program that asks the user how many credits they have taken. If they have taken 23
or less, print that the student is a freshman. If they have taken between 24 and 53, print that
they are a sophomore. The range for juniors is 54 to 83, and for seniors it is 84 and over.
'''

no_of_credits=int(input("Enter the number of credits: "))
if(no_of_credits<=23):
    print("The student is a Freshman.")
elif(no_of_credits>=24 and no_of_credits<=53):
    print("They are a sophomore.")
elif(no_of_credits>=54 and no_of_credits<=83):
    print("They are juniors.")
else:
    print("They are seniors.")