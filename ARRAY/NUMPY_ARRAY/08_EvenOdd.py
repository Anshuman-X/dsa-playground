from numpy import *
n=int(input("Enter the size: "))
val=zeros(n,dtype=int)

for i in range(n):
    val[i]=int(input("Enter the elements: "))
    
print("Even elements are ")
for x in val:
    if(x%2==0):
        print(x,end=" ")

print("\n")
print("Odd elements are ")
for x in val:
    if(x%2 !=0):
        print(x,end=" ")