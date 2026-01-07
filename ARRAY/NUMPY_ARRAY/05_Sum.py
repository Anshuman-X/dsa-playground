from numpy import *

n=int(input("Enter the size: "))
val=zeros(n,dtype=int)

sum=0
for i in range(n):
    val[i]=int(input("Enter the elements: "))
    
for x in val:
    sum=sum+x
    
print("sum of elements: ",sum)