class Solution(object):
    def addBinary(self, a, b):
        total = ""
        x = str(a)[::-1]
        y = str(b)[::-1]
        for i in len(x):
            for j in len(y):
                if i == j:
                    if x[i] == "0" and y[j] == "0":
                        total += "0"
                    elif x[i] == "1" and y[j] == "0" or x[i] == "0" and y[j] == "1":
                        total += "1"
                    else:
                        total += "01"
        revtotal = str(total)[::-1]
        print(total)
        return 0


a = "11"
b = "1"
p = Solution()
p.addBinary(a, b)
