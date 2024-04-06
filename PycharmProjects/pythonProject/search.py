from array import *

arr = array("i", [])

size = int(input("Enter the size of the array "))

for i in range(size):
    value = int(input("Enter the next value "))
    arr.append(value)
    
print(arr)

k = 0
index = int(input("Enter value to search it's index "))
for a in arr:
    if (a == index):
        print(k)
        break
    k += 1
