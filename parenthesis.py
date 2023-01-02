
'''
People often forget closing parentheses when entering formulas. Write a program that asks
the user to enter a formula and prints out whether the formula has the 
same number of opening and closing parentheses.
'''

formula=input("Enter a formula: ")

open_parenthesis=formula.count("(")
close_parenthesis=formula.count(")")

if(open_parenthesis==close_parenthesis):
    print("The formula has the same number of opening and closing parentheses.")
    
else:
    print("The formula do not have the same number of opening and closing parentheses.")