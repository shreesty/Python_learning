'''
Write a program that asks the user to guess a random number between 1 and 10. If they guess
right, they get 10 points added to their score, and they lose 1 point for an incorrect guess. Give
the user five numbers to guess and print their score after all the guessing is done.

'''
score=0
from random import randint
num=randint(1,10)

for i in range(1,6):
    number=int(input("Enter a random number between 1 and 10: "))
    
    if (num==number):
        #print("You got 10 points added to your score.")
        score=score + 10
        print("Your total_score is : ",score)
    else:
        #print("You lose 1 point for an incorrect guess")
        score=score-1
        print("Your total_score is : ",score)

print("Random_number is: ",num)