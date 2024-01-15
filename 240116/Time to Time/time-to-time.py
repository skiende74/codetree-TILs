hour, mins, hour_goal, mins_goal

elapsed_time = 0

while True:
    if (hour, mins) == (hour_goal, mins_goal):
        break
    
    elapsed_time += 1
    mins += 1

    if mins == 60:
        hour += 1
        mins -= 60

print(elapsed_time)