from array import *
val=array('i',[1,2,3,4,5,6])
val.insert(3,9)            # No data overflow in array i.e no element is removed from array
print("After insertion: ")
for x in val:
    print(x,end=" ")
    
print("\n")
val.append(50)
print("After append: ")
for x in val:
    print(x,end=" ")

print("\n")
val[2]=20
print(val)

print("\n")

val.pop(3)               # uses index
print("After pop: ")
for x in val:
    print(x,end=" ")
    
print("\n")

val.remove(50)           # uses element
print("After remove: ")
for x in val:
    print(x,end=" ")
    
print("\n")
print(val.index(5))      # To search index number of the element