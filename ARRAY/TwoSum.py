def TwoSum(arr,target):
    seen = {}
    
    for i in range(len(arr)):
        need = target - arr[i]
        if need in seen:
            return [seen[need],i]
        else:
            seen[arr[i]] = i

arr = [2,3,4,5,6]
print(TwoSum(arr,9))
