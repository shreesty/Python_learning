'''
Write a program that asks the user for a number of seconds and prints out how many minutes
and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
operator to get minutes and the % operator to get seconds.]
'''
seconds=int(input("Enter a number of seconds: "))
if(seconds%60==0):
    minutes= seconds/60
    print("Minutes: ",minutes)
else:
    minutes= seconds//60
    seconds1=seconds-minutes* 60
    print("Minutes: ",minutes)
    seconds1=seconds-minutes* 60
    print("Seconds: ",seconds1)