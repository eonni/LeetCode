class Solution:
    def __init__(self, celsius: float):
        self.celsius = celsius

    def convertTemperature(self):
        return [self.celsius + 273.15, (self.celsius * 1.80) + 32.00]


a = Solution(36.50)
b = Solution(122.11)
print(a.convertTemperature())
print(b.convertTemperature())
