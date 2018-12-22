def factorial_mod_ten(n):
    if n >= 5: return 0
    mod = n % 10
    for i in range(1, n):
        mod *= i
        mod = mod % 10
    return mod

for i in range(int(input())):
    print(factorial_mod_ten(int(input())))
