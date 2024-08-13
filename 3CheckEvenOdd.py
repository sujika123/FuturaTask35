# Write a Python program that determines whether a given number (accepted from the user) is even or odd,
# and prints an appropriate message to the user.

n = int(input("Enter the number : "))
if(n%2 == 0):
    print(n,"is even number")
else:
    print(n, "is odd number")