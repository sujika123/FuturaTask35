#Write a program that prompts the user for a number and then prints a countdown from that number to 5.


n = int(input("Enter the number : "))
for i in range(n,4,-1):
    print(i)