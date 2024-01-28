num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

month, day,goal_month, goal_day = map(int, input().split())
elapsed_days = 1
while True:
    if (month,day) == (goal_month, goal_day):
        break

    elapsed_days += 1
    day += 1
    if day > num_of_days[month]:
        month += 1
        day = 1

print(elapsed_days)