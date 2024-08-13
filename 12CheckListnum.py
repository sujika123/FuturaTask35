#Check if the first and last number of a list is the same


list = []
n = int(input("Enter number of elements in a list : "))
print("Enter elements of list ")
for i in range(n):
    list.append(int(input()))
print(list)
if(list[0] == list[-1]):
    print("first and last number of a list is same")
else:
    print("first and last number of a list is not same")