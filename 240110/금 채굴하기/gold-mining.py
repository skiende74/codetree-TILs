# 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

#
def mine(i,j): 
    earn = -(K**2 + (K+1)**2)
    count = 0
    for di in range(-K, K+1):
        for dj in range(-K+abs(di), K-abs(di)+1):
            if 0<=i+di<N and 0<=j+dj<N:
                if grid[i+di][j+dj]:
                    count += 1
    earn += count*M

    return count if earn>=0 else 0


            


# 본문
count_max = 0
for K in range(1, N+1):
    for i in range(0, N):
        for j in range(0, N):
            count_max = max(count_max, mine(i,j))

print(count_max)