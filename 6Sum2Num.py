#Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))

sum = a + b
if (sum >= 15 and sum <= 20):
    print("Sum = ",20)
else:
    print("Sum = ",sum)