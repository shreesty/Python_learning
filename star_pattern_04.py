'''
Use a for loop to print an upside down triangle like the one below. Allow the user to specify
how high the triangle should be.

****
***
**
*

'''
for i in range(1,5):
    for j in range(5-i):
        print("*",end="")
    print("")