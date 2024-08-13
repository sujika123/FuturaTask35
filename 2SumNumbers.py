#Write a Python program to calculate the sum of three given numbers. If the values are equal,
# return three times their sum.


a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))

sum = a + b + c
if(a == b == c):
    s = 3 * sum
    print("Sum is : ",s)
else:
    print("sum is : ",sum)

