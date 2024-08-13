# Write a Python program to count the number 4 in a given list
# List = [2,3,4,2,4,5,3,5,3,4,4]


List = [2,3,4,2,4,5,3,5,3,4,4]
count = 0
for i in List:
    if i == 4 :
        count = count + 1
print(count)