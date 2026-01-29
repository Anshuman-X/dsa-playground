def Min_Max(arr):
    arr.sort()
    n = len(arr)
    
    max =0
    i = 0
    j = n-1
    while (i <= n//2 and j >= n//2):
        max = max + abs(arr[i]-arr[j])
        i = i+1
        j = j-1
    
    print("Maximum difference is ",max)
    
    i = 0
    j = i+1
    min = 0
    while(i<=n//2):
        min = min + abs(arr[i]-arr[j])
        
        i = i+2
    print("Minimum difference is ",min)

arr = []
num = int(input("Enter the size: "))
for i in range(num):
    ap = int(input("Enter the elements: "))
    arr.append(ap)

print(arr)

Min_Max(arr)