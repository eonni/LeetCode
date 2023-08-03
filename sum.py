class Solution:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2


a = Solution(12, 5)
b = Solution(-10, 4)
print(a.sum())
print(b.sum())
