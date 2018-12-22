import math

L = int(input())
D = int(input())
X = int(input())

def digit_sum(n):
    n = str(n)
    digit_sum = sum([int(digit) for digit in n])
    return digit_sum

N_attempt = math.ceil(L)
M_attempt = math.floor(D)
N_found = False
M_found = False

for i in range(D-L+1):
    if digit_sum(N_attempt) == X:
        N_found = True
    if digit_sum(M_attempt) == X:
        M_found = True

    if not N_found: N_attempt += 1
    if not M_found: M_attempt -= 1

    if N_found and M_found:
        break

print(N_attempt)
print(M_attempt)
