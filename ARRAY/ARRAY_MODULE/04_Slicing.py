from array import *
val=array("u",['a','b','c','d','e','f'])

s=val[1:6]
for i in s:
    print(i,end=" ")

print("\n")
l=val[0:6:2]
for x in l:
    print(x,end=" ")
    
print("\n")

# To reverse the array

val2=val[::-1]
for m in val2:
    print(m,end=" ")