## Output: 5, nums = [0,1,4,0,3,_,_,_]
# def removeelements(nums,val):
#     n = len(nums)
    
#     i = 0
#     while i < n:
#         if val == nums[i]:
#             nums.pop(i)
#         else:
#             i = i+1
#     return len(nums),nums

# nums = [0,1,2,2,3,0,4,2] 
# k = removeelements(nums,2)
# print(k)

def removeelements(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)   # remove current index
        else:
            i += 1        # move forward only if not removed
    return len(nums), nums

nums = [0,1,2,2,3,0,4,2]
k = removeelements(nums, 2)
print(k)
