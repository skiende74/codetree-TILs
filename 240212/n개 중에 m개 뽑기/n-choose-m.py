N, M = map(int, input().split())

combination = []
def choose(i):
    global combination

    if i == N+1:
        if len(combination)==M:
            print(' '.join(combination))
        return
    

    combination.append(str(i))
    choose(i + 1)
    combination.pop()

    choose(i + 1)

choose(1)