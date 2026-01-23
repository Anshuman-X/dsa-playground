def BubbleSort(a):
    n = len(a)
    
    for i in range(n):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
   
a = [64,32,25,45,40,51,2]
print("Before Sorting: ")             
print(a)
BubbleSort(a)
print("After Sorting:")
print(a)