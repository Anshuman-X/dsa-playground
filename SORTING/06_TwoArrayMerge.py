def merge(arr,m,arr2,n):
    idx = n+m-1
    i = m-1
    j = n-1
    
    while i >= 0 and j >= 0:
        if arr[i] > arr2[j]:
            arr[idx] = arr[i]
            i = i-1
        else:
            arr[idx] = arr2[j]
            j = j-1
        
        idx = idx-1
    while j>=0:
        arr[idx] = arr2[j]
        j = j-1
        idx = idx-1
        
arr1=[2,5,8,0,0,0]
arr2=[1,3,4]
merge(arr1,3,arr2,3)
print(arr1)