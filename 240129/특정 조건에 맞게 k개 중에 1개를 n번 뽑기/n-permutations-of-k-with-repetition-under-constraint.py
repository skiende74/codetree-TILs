import sys

sys.setrecursionlimit(10000)
K, N = map(int, input().split())

def choose(num):
    if num==N:
        print(' '.join(answer))
        return

    for i in range(1,K+1):
        if num<=N-2 or answer[-(3-1):] != [str(i)]*(3-1):
            answer.append(str(i))
            choose(num+1)
            answer.pop()
    
answer = []
choose(0)