from numpy import *
val=array([1,2,3,4,5])
for x in val:
    print(x,end=" ")
    
print("\n")
val=linspace(10,20,5)
for x in val:
    print(x,end=" ")
    
print("\n")

val=arange(10,30,5)
for x in val:
    print(x,end=" ")
    
print("\n")

val=zeros(10)
print(val)

val1=ones(5)
print(val1)

val=full(10,3)
print(val)