def isTrionic(nums):
    n = len(nums)

    if n < 3:
        return False

    p = -1
    q = -1

    
    for i in range(1, n):
        if nums[i] > nums[i - 1]:
            continue
        else:
            p = i - 1
            break

    if p == -1 or p == 0:
        return False

    
    for i in range(p + 1, n):
        if nums[i] < nums[i - 1]:
            continue
        else:
            q = i - 1
            break

    if q == -1 or q == n - 1:
        return False

   
    for i in range(q + 1, n):
        if nums[i] <= nums[i - 1]:
            return False

    return True


nums = [2, 1, 3]
print(isTrionic(nums))

# nums = [1,3,5,4,2,6]
# print(isTrionic(nums))