def moveZeroes(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            for j in range(len(nums) - 1):
                nums[j] = nums[j + 1]
            nums[len(nums) - 1] = 0
