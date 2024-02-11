N, M = map(int, input().split())

curr_num = []
used = [False]*(N+1)
def choose():
    global curr_num

    if len(curr_num)==M:
        num = curr_num
        num = ' '.join(num)
        print(num)
        return
    
    for i in range(1,N+1):
        if not used[i] and (len(curr_num) == 0 or int(curr_num[-1]) < i):
            used[i]=True
            curr_num.append(str(i))
            choose()
            used[i]=False
            curr_num = curr_num[:-1]
choose()