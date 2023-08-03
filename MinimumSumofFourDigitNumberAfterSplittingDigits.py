def minimumSum(num):
    dig = str(num)
    a = b = 0
    d = sorted(dig)
    a = int(d[0]) * 10 + int(d[2])
    b = int(d[1]) * 10 + int(d[3])
    return a + b


num1 = minimumSum(2932)
num2 = minimumSum(4009)
print(num1)
print(num2)
