n1, n2 = input().split()

n1, n2 = n1[::-1], n2[::-1]

if (int(n1) > int(n2)):
    print(n1)
else:
    print(n2)
