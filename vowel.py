
'''
Write a program that asks the user to enter a word and prints out whether that word contains
any vowels.
'''
word=input("Enter a word: ")
if any(char in 'aeiouAEIOU' for char in word):
    print("The word contains vowels.")
else:
    print("The word doesnot contains ")