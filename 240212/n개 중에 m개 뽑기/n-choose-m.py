N, M = map(int, input().split())

combination = []
def choose(curr_num, cnt):
    global combination

    if curr_num == N+1:
        if cnt==M:
            print(' '.join(combination))
        return
    

    combination.append(str(curr_num))
    choose(curr_num + 1, cnt+1)
    combination = combination[:-1]

    choose(curr_num + 1, cnt)

choose(1,0)