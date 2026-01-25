def Divide(arr,l,r):
    if l < r:
        m = (l+r)//2
        
        Divide(arr,l,m)
        Divide(arr,m+1,r)
        Merge(arr,l,m,r)
        
def Merge(arr,l,m,r):
    s1 = m-l+1
    s2 = r-m

    L = [0]*s1
    R = [0]*s2

    for i in range(s1):
        L[i] = arr[l+i]
    for j in range(s2):
        R[j] = arr[m+1+j]
        
    i = j =0
    k = l
    while i < s1 and j < s2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i = i+1
            k = k+1
        else:
            arr[k] = R[j]
            j = j+1
            k = k+1
    while(i<s1):
        arr[k] = L[i]
        i = i+1
        k = k+1
    while(j<s2):
        arr[k] = R[j]
        j = j+1
        k = k+1

arr = [67,5,9,1,56,34,61]
print("Original Array:",arr)
start = 0
end = len(arr)-1
Divide(arr,start,end)
print("After Sorting:",arr)