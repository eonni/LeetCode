class Solution:
    def __init__(self, operations):
        self.operations = operations

    def finalValueAfterOperations(self):
        x = 0
        for i in self.operations:
            if i == "++X" or i == "X++":
                x += 1
            else:
                x -= 1
        return x


a = Solution(["--X", "X++", "X++"])
b = Solution(["++X", "++X", "X++"])
c = Solution(["X++", "++X", "--X", "X--"])
print(a.finalValueAfterOperations())
print(b.finalValueAfterOperations())
print(c.finalValueAfterOperations())
