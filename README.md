class Solution(object):
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self):
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if i != j and self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
