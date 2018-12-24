sum = 0
for i in range(int(input())):
    num = int(input())
    base, exponent = (num - (num % 10))/10, num % 10
    term = int(base ** exponent)
    sum += term

print(sum)
