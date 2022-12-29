
'''
Write a program that asks the user to enter a string. The program should then print the
following:
(a) The total number of characters in the string
(b) The string repeated 10 times
(c) The first character of the string (remember that string indices start at 0)
(d) The first three characters of the string
(e) The last three characters of the string
(f) The string backwards
(g) The seventh character of the string if the string is long enough and a message otherwise
(h) The string with its first and last characters removed
(i) The string in all caps
(j) The string with every a replaced with an e
(k) The string with every letter replaced by a space
'''

string=input("Enter a string: ")
print("The total number of characters in the string is : ",len(string))

print("The string repeated 10 times: ", string * 10)
print("The first character of the string: ",string[0])
print("The first three characters of the string: ",string[ :3])
print("The last three characters of the string: ",string[-3: ])
print("The string backwards: ",string[ ::-1])
print("The seventh character of the string: ",string[6])
first_char_removed=string.replace(string[0],"")
print("The string with its first removed: ",first_char_removed)
last_char_removed=first_char_removed.replace(string[-1],"")
print("The string with its first and last removed:",last_char_removed)
print("The string in all caps: ",string.upper())
print("The string with every a replaced with an e: ",string.replace("a","e"))
print("The string with every letter replaced by a space: ",*[i for i in string],sep=" ")