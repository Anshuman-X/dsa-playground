# def FindTarget(nums,target):
#     n = len(nums)
    
#     for i in range(n):
#         if nums[i]==target:
#             return i
        
#         elif nums[i]>target:
#             return i 
        
#     else:
#         nums.append(target)
#         return nums.index(target)
        
        
def FindTarget(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

nums= [1,3,5,6]
print(FindTarget(nums,5))