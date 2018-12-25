leader = 0
high_sum = 0
for i in range(5):
    contestant = i+1
    grade = sum([int(x) for x in input().split()])
    if grade > high_sum:
        leader = contestant
        high_sum = grade

print(leader, high_sum)
