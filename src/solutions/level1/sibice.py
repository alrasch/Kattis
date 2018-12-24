import math

num_matches, w, h = [int(x) for x in input().split()]

max_length = math.sqrt(w*w + h*h)

for i in range(num_matches):
    length = int(input())

    if length <= max_length: print("DA")
    else: print("NE")
