
'''
A simple way to estimate the number of words in a string is to count the number of spaces
in the string. Write a program that asks the user for a string and returns an estimate of how
many words are in the string.
'''

string=input("Enter a string: ")
count_space=string.count(" ")
count_words = count_space + 1
print("The number of words are in the string: ",count_words)