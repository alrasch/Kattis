cost = float(input())
lawns = int(input())

total_cost = 0
for i in range(lawns):
    w, l = input().split()
    w = float(w)
    l = float(l)
    sqm = w*l
    price = cost * sqm
    total_cost += price
print(total_cost)
