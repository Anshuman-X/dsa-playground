def MinMax(arr):
    n =  len(arr)
    max = arr[0]
    for i in range(n):
        if max < arr[i]:
            max = arr[i]
    
    min = arr[0]
    for i in range(n):
        if min > arr[i]:
            min = arr[i]
            
    sum = 0
    for x in arr:
        sum = sum+x
        
    return sum-max,sum-min
    
n = input()
arr = list(map(int,input().split()))
print(MinMax(arr))