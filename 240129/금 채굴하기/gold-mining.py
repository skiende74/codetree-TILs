import sys

N, M = map(int, input().split())
grid = [list(map(int,input().split())) for _ in range(N)]

#
max_gold = 0
for i in range(N):
    for j in range(N):
        for K in range(N):

            earn = -(K*K + (K+1)*(K+1))
            gold = 0
            for di in range(-K, K+1):
                for dj in range(-K, K+1):
                    i2,j2 = i+di, j+dj
                    if 0<=i2<N and 0<=j2<N and abs(di)+abs(dj)<=K and grid[i2][j2]==1:
                        earn += M
                        gold += 1
            if earn>=0:
                max_gold = max(max_gold, gold)

print(max_gold)