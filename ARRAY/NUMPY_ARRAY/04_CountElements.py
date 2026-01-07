from numpy import *

n=int(input("Enter the size of array: "))
val=zeros(n,dtype=int)

count=0
for i in range(n):
    val[i]=int(input("enter the elementts: "))
    count=count+1
    
print("Number of elements: ",count)