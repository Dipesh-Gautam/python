num = 5
print(num)
print(id(num)) 

name = "xyz"
print(name)
print(id(name))
abc = id(name)
print(abc)


value1 = 10
value2 = value1
value3 = 10
print("value1 =",value1)
print("value1 address =",id(value1))
print("value2 = value1 =",value2)
print("value2 address =",id(value2))
print("value3 =",value3)
print("value3 address =",id(value3))
print("address of 10 =",id(10))
