n = int(input())

base = 2 + sum([2**i for i in range(n)])
power = base**2

print(power)
