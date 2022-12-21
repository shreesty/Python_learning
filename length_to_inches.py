
'''Write a program that asks the user to enter a length in centimeters. If the user enters a negative
length, the program should tell the user that the entry is invalid. Otherwise, the program
should convert the length to inches and print out the result. There are 2.54 centimeters in an inch.
'''
length_in_cm=float(input("Enter the length in centimeters: "))

length_in_inches= length_in_cm/2.54
if(length_in_cm < 0):
    print("Entry is invalid")
else:
    print("length_in_inches: ",length_in_inches)