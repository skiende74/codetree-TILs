m1,d1, m2,d2 = map(int,input().split())

num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def get_elapsed_day(m1,d1):
    elapsed_day = 0
    for i in range(1, m1):
        elapsed_day += num_of_days[i]
    elapsed_day += d1
    return elapsed_day

diff = get_elapsed_day(m2,d2) - get_elapsed_day(m1,d1)
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

i = (0+diff)%7
print(day_of_week[i])