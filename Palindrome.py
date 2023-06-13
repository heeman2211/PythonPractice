#Palindrome Checker: Write a function that takes a string as input and checks whether it is a palindrome (reads the same forwards and backwards). Return True if it is, and False otherwise.
a = input("Enter your string\nYour String can have capital letters or lowercase letters:\n\n")
b = a.lower()
print(b == b[::-1])