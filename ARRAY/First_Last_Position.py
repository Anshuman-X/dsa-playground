def searchRange(nums,target):
    if target not in nums:
        return [-1,-1]
    
    first = -1
    last = -1
    for i in range(len(nums)):
        if target == nums[i]:
            if first == -1:
                first = i
            last = i
    return first,last
        

nums = [5,7,7,8,8,10]
print(searchRange(nums,8))