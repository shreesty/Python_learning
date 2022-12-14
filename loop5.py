# . Write a program to fill the screen horizontally and vertically with your name. 

name= input("Enter your name: ")
for i in range(1,50):
    for j in range(1,50):
        print(name, end="")