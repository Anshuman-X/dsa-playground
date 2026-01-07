from array import *
val=array("i",[1,2,3,4,5,6])
print("Elements in first array: ")
for x in val:
    print(x,end=" ")
print("\n")
copyarr=array(val.typecode,(x for x in val))
print("Elements in copied array: ")
for x in copyarr:
    print(x,end=" ")