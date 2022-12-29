
'''
Write a program that asks the user to enter two strings of the same length. The program
should then check to see if the strings are of the same length. If they are not, the program
should print an appropriate message and exit. If they are of the same length, the program
should alternate the characters of the two strings. For example, if the user enters abcde and
ABCDE the program should print out AaBbCcDdEe
'''

string1=input("Enter 1st string: ")
string2=input("Enter 2nd string: ")

if(len(string1)!=len(string2)):
    print("The length of the two strings are not equal")
else:
    print(string2[0]+string1[0]+string2[1]+string1[1]+string2[2]+string1[2]+string2[3]+string1[3]+string2[4]+string1[4]    )