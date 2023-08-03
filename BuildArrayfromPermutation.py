class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def buildArray(self):
        ans = []
        for i in range(len(self.nums)):
            ans.append(self.nums[self.nums[i]])
        print(ans)


nums1 = Solution([0, 2, 1, 5, 3, 4])
nums2 = Solution([5, 0, 1, 2, 3, 4])
nums1.buildArray()
nums2.buildArray()
