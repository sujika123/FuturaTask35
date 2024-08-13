#Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

sum = a + b + c
if (a == b) or (b == c) or (a == c):
    sum = 0
    print("Sum = ",sum)
else:
    print("Sum = ",sum)





