
'''
Ask the user to enter a list of strings. Create a new list that consists of those strings with their
first characters removed.
'''
list=[]
list=input("Enter a list of strings: ")
list=list.split(",")

print(list)
print("List after removing the 1st characters from each string: ")
for i in range(len(list)):
    new_list=(list[i][1: ])

    print(new_list)