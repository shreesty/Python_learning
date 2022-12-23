'''
Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
4 and how many end in a 9.
'''

count=0
for i in range(1,100):
    squares=i*i
    if(squares%10==4):
        count=count+1
        #print(squares)
print("No of Squares from 1 to 100 end in a 4 is: ",count)

count=0
for i in range(1,100):
    squares=i*i
    if(squares%10==9):
        count=count+1
        #print(squares)
print("No of Squares from 1 to 100 end in a 9 is: ",count)

