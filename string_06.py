'''
Write a program that asks the user to enter their name in lowercase and then capitalizes the
first letter of each word of their name.
'''
name=input("Enter a name in lowercase: ")

words=name.split()
capitalized_word=[word.capitalize() for word in words]
capitalized_name=" ".join(capitalized_word)
print(capitalized_name)

