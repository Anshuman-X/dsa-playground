from numpy import *

n=int(input("Enter the size of array: "))
val=zeros(n,dtype=int)

for i in range(n):
    val[i]=int(input("Enter the elements: "))
    
for i in val:
    print(i,end=" ")
    
n=HELLO
print("n")