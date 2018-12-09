import math

articles, desired_impact = [int(x) for x in input().split()]

bribes = 0
while True:
    impact = math.ceil(bribes / articles)

    if impact >= desired_impact:
        print(bribes)
        break
    else:
        bribes += 1
