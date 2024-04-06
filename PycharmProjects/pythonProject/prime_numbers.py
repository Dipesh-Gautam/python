x = int(input("Enter any number to check wheather it is prime or not "))
print("Entered number is ", x)

for i in range(2, x):
    if x % i == 0:
        print("not prime")
        break
else:
    print("prime")
