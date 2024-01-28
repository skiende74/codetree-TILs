import sys

N = int(input())
seq = [int(input()) for _ in range(N)]

def dfs(selected):
    if len(selected) == N:
        calc(selected)
        return
    
    selected.append(True)
    dfs(selected)
    selected.pop()
    
    selected.append(False)
    dfs(selected)
    selected.pop()

def calc(selected):
    global count
    total = 0

    for num, select in zip(seq, selected):
        if select:
            str_num = str(num)
            str_total = str(total)
            N2 = min(len(str_num),len(str_total))
            for i in range(N2):
                if int(str_num[-i-1]) + int(str_total[-i-1]) >= 10:
                    return
            total += num
    count = max(count, sum(selected))

count = 0
dfs([])
print(count)