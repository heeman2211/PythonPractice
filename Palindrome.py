#Palindrome Checker: Write a function that takes a string as input and checks whether it is a palindrome (reads the same forwards and backwards). Return True if it is, and False otherwise.
# Defining the function
def pal(x):
    b = x.lower()
    return (b == b[::-1])
a = input("Enter your string\nYour String can have capital letters or lowercase letters:\n\n")
print(pal(a))