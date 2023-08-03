class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def numIdenticalPairs(self):
        count = 0
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if i < j and self.nums[i] == self.nums[j]:
                    count += 1
        print(count)


nums1 = Solution([1, 2, 3, 1, 1, 3])
nums2 = Solution([1, 1, 1, 1])
nums3 = Solution([1, 2, 3])
nums1.numIdenticalPairs()
nums2.numIdenticalPairs()
nums3.numIdenticalPairs()
