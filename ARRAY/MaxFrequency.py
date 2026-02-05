def maxFrequency(nums):
    n = len(nums)
    
    maxEl = 0
    maxFreq = 0
    
    visited = [False]*n
    for i in range(n):
        if visited[i]:
            continue

        freq = 0
        for j in range(i,n):
            if nums[i] == nums[j]:
                freq = freq+1
                visited[j] = True

        if freq > maxFreq:
            maxFreq = freq
            maxEl = nums[i]
        elif freq == maxFreq:
            maxEl = min(maxFreq,nums[i])
    return maxFreq

nums = [1,2,4]

print(maxFrequency(nums))