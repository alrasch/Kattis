x = int(input())
n = int(input())

available = 0
for i in range(n):
    available += x
    expenditure = int(input())
    available -= expenditure
print(available + x)
