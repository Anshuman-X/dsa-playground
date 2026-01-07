from numpy import *

n=int(input("Enter the size: "))
val=zeros(n,dtype=int)

for i in range(n):
    val[i]=int(input("Enter the elements: "))
    
min_value=val[0]
for i in range(1,n):
    if(min_value>val[i]):
        min_value=val[i]
        
print("Smallest element is: ",min_value)