#Write a program to print multiplication table of a given number

n = int(input("Enter number : "))

for i in range(1,11,1):
    print(i,"*",n,"=",i*n)