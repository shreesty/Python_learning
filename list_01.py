'''
Write a program that asks the user to enter a list of integers. Do the following:
(a) Print the total number of items in the list.
(b) Print the last item in the list.
(c) Print the list in reverse order.
(d) Print Yes if the list contains a 5 and No otherwise.
(e) Print the number of fives in the list.
(f) Remove the first and last items from the list, sort the remaining items, and print the
result.
(g) Print how many integers in the list are less than 5.
'''
list=[]
list= (input("Enter a list: "))
list=[x for x in list]
print(list)
print("Total number of items in the list: ",len(list))
print("Last item in the list: ",list[-1])
print("List in reverse order: ",list[ ::-1])

if("5" in list):
    print("Yes, the list contains a 5.")
else:
    print("No, the list doesnot contains a 5.")

count=0
for i in range(len(list)):
    if int(list[i])==5:
        count=count+1
print("Number of fives: ",count)
    
list.remove(list[0])
list.remove(list[-1])
print("List after removing 1st and last element: ",list)
list.sort()
print("Remaining sorted list: ",list)

count=0
for i in range(len(list)):
    if int(list[i])<5:
        count=count+1
print("Number of integers in the list are less than 5:",count)