def removeduplicate(nums):
    n = len(nums)
    if n == 1:
        return 1
    
    nums.sort()
    i = 0
    j = i+1
    while j < n:
            if nums[j] != nums[i]:
                i = i+1
                nums[i],nums[j] = nums[j],nums[i]
            j = j+1
    return i+1

nums = [2,5,1,4,5,1,4]
print(removeduplicate(nums),nums)