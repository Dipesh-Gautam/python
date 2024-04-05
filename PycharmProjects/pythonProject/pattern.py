x = "#"
for i in range(0,4):
    for j in range(0,4):
        print(x,end=" ")  
    print()  
print()

for a in range(4):
    for b in range(a+1):
        print(x,end=" ")
    print()
    
print()

for m in range(0,4):
    for n in range(4-m):
        print(x,end=" ")
    print()