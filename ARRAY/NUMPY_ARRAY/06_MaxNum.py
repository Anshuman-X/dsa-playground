from numpy import *

n=int(input("Enter the size: "))
val=zeros(n,dtype=int)

for i in range(n):
    val[i]=int(input("Enter the elements: "))
    
print(val)

max_value=val[0]

for i in range(1,n):
    if(max_value<val[i]):
        max_value=val[i]
        
print(max_value)