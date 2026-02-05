def transform_array(nums):
    n = len(nums)
    
    result = []
    for i in range(n):
        if nums[i] != 0:
            target_index = (i+nums[i]+n)%n
            result.append(nums[target_index])
        else:
            result.append(0)
            
    return result


nums = [3,-2,1,1]
print(transform_array(nums))
            