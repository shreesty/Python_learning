

# /////////////////////

'''
Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.

Enter a number: 7
7---14---21---28---35

'''
x=int(input("Enter a number: "))

print(*[i*x for i in range(1,6)],sep="---")
# print(x*1, x*2, x*3,x*4,x*5,sep="---")