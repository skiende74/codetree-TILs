N = int(input())
dscores = [input().split() for _ in range(N)]

score= [0, 0]
max_score = 0
max_idxs = [1,2]

ans = 0
state = 2
for dscore in dscores:
    person, ds = dscore
    ds = int(ds)
    
    state_old = state

    if person == 'A':
        score[0] += ds
    else:
        score[1] += ds
    
    if score[0] > score[1]:
        state = 1
    elif score[0] == score[1]:
        state = 2
    else:
        state = 3
    if state != state_old:
        ans+=1


print(ans)