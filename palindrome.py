
'''
Write a program that asks the user to enter a word and determines whether the word is a
palindrome or not. A palindrome is a word that reads the same backwards as forwards.
'''
word=input("Enter a word: ")
word1=word[::-1]
if (word==word1):
    print("It is a plindrome.")
else:
    print("Not Palindrome")