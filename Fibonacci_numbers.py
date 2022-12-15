
'''The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
number thereafter is the sum of the two preceding numbers. Write a program that asks the
user how many Fibonacci numbers to print and then prints that many.

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
'''
initial=0
final=1
fibonachi=initial + final

num=int(input("Enter a number for how long fibonaachi numbers to be printed: "))

for i in range(num):
    print(fibonachi,end=",")
    fibonachi=initial + final
    initial=final
    final=fibonachi