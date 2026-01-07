from array import *

arr=array("i",[])
n=int(input("Enter the size of array: "))

for i in range(0,n):
    arr.append(int(input("Enter the elements: ")))
    
for x in arr:
    print(x,end=" ")