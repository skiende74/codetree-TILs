goal_a, goal_b, goal_c = list(map(int,input().split()))

a,b,c = 11,11,11
elapsed_minutes = 0
while True:
    if (a,b,c) == (goal_a, goal_b, goal_c):
        break
    
    elapsed_minutes += 1
    c += 1
    if c == 60:
        c= 0
        b+=1
    if b == 24:
        b = 0
        a += 1

print(elapsed_minutes)