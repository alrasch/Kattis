n = int(input())
total = 0
for i in range(n):
    qol, years = input().split()
    total += float(qol) * float(years)
print(total)
