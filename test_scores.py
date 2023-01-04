
'''
Ask the user to enter 10 test scores. Write a program to do the following:
(a) Print out the highest and lowest scores.
(b) Print out the average of the scores.
(c) Print out the second largest score.
(d) If any of the scores is greater than 100, then after all the scores have been entered, print
a message warning the user that a value over 100 has been entered.
(e) Drop the two lowest scores and print out the average of the rest of them.
'''
scores = []
for i in range(10):
    score = int(input("Enter a test score: "))
    scores.append(score)

highest=max(scores)
print("Highest Score: ",highest)

lowest=min(scores)
print("Lowest Score: ",lowest)
 
average= sum(scores)/len(scores)
print("Average of the scores: ",average)

scores.sort()
second_highest=scores[-2]
print("Second largest score: ",second_highest)


if(scores[i]>100):
    print("A value over 100 has been entered.")

scores=scores[2: ]
print(scores)
average1=sum(scores)/len(scores)
print("Average of the rest: ",average1)





