from array import *

values = array("i", [2, 5, 6, 7, 2, 6, 9])

for m in values:
    print(m)

print()

new_array = array(values.typecode, (a for a in values))

for b in new_array:
    print(b)
