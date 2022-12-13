
#print the following pattern: 
'''
*******************
*                 *
*                 *
*******************

'''

for i in range(5):
    for j in range(20):
        if((i==0 or i==4) or (j==0 or j==19)):
            print("*",end="")
        else:
            print(" ",end="")
    print(" ")
