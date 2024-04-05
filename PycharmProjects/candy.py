available = 25
x = int(input("Enter how many candies you want?"))
i = 1
while(i<=x):
    if (i>available):
        print("Out of stock")
        break
    
    print("candies",i)
    i += 1

print("Take the avialable candies and enjoy")