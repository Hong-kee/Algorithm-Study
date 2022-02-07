def removeDuplicates(nums):
    start = 0
    for end in range(len(nums)):
        if start < 2 or nums[end] > nums[start-2]:
            nums[start] = nums[end]
            start += 1
    return start

nums = [1,1,1,2,2,3]
k = removeDuplicates(nums)
print(k, nums)