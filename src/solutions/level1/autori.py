input = input()
name = ''.join(x for x in input if not x.islower() and x != '-')
print(name)
