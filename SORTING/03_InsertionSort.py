def InsertionSort(a):
    n = len(a)
    
    for i in range(1,n):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key

arr = [5,1,7,3,9,2]
InsertionSort(arr)
print(arr)