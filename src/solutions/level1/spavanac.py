time = input()

hour, minute = [int(x) for x in time.split()]

result_hour = hour if minute >= 45 else hour - 1

result_hour %= 24

result_minute = (minute - 45) % 60

print(result_hour, result_minute)
