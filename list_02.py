
'''
Write a program that generates a list of 20 random numbers between 1 and 100.
(a) Print the list.
(b) Print the average of the elements in the list.
(c) Print the largest and smallest values in the list.
(d) Print the second largest and second smallest entries in the list
(e) Print how many even numbers are in the list.
'''

from random import randint
list=[]

for i in range(20):
    list.append(randint(1,100))
print("List: ",list)
print("The average of the elements in the list: ",sum(list)/len(list))
print("The largest values in the list: ",max(list))
print("The smallest values in the list: ",min(list))

#print 2nd largest 2nd smallest entries in the list??
list.sort()
print("The second largest values in the list: ",list[-2])
print("The second smallest values in the list: ",list[1])

count=0
for i in range(len(list)):
    if(list[i]%2==0):
        count+=1
print("The number of even numbers in the list: ",count)
