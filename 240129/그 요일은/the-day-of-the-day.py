num_of_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
m1,d1,m2,d2 = map(int, input().split())
day_of_week = input()
dow2idx = {'Mon':0,'Tue':1,'Wed':2,'Thu':3, 'Fri':4,'Sat':5, 'Sun':6}
i_goal = dow2idx[day_of_week]
m,d = m1, d1

i = 0
count_day_of_week = 0
if i_goal == 0:
    count_day_of_week += 1
while True:

    if (m,d) == (m2,d2):
        print(count_day_of_week)
        break
    
    d+=1
    i = (i+1)%7
    if i == i_goal:
        count_day_of_week += 1
    if d>num_of_days[m]:
        d=1
        m+=1