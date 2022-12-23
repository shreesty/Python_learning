'''
Write a program that asks the user for an hour between 1 and 12, asks them to enter am or pm,
and asks them how many hours into the future they want to go. Print out what the hour will
be that many hours into the future, printing am or pm as appropriate. An example is shown
below.

Enter hour: 8
am or pm ?
How many hours ahead? 5
New hour: 1 pm
'''

time=int(input("Enter a number between 1 to 12: "))
indicator= input("Enter AM or PM: ")
future_hours=int(input("Enter how many hours into the future you want to go: "))
final_time=(time + future_hours)
if(final_time> 12):
    if(indicator=="AM"):
        indicator="PM"
        print(final_time -12,indicator)
    else:
        indicator="AM"
        print(final_time -12,indicator)
else:
    if(indicator=="AM"):
        indicator="AM"
        print(final_time,indicator)
    else:
        indicator="PM"
        print(final_time,indicator)