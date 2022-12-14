'''
Write a program that uses exactly four for loops to print the sequence of letters below:
AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
'''
for i in range(1,11):
    print("A",end="")
for i in range(1,8):
    print("B",end="")
for i in range(1,5):
    if(i!=5):
        print("CD",end="")
    else:
        print("E",end="")
for i in range(1,7):
    if(i!=6):
        print("F",end="")
    else:
        print("G",end="")

