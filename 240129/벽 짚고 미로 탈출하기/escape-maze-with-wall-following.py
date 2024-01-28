N = int(input())
r,c = map(int,input().split())
grid = [list(input()) for _ in range(N)]

r,c= r-1,c-1
i,j=r,c

dir2vec = [[0,1],[-1,0],[0,-1,],[1,0]]
direction = 0
count = 0
visited = [[[False]*4 for _ in range(N)] for _ in range(N)]

while True:
    if visited[i][j][direction]:
        count = -1
        break
    di,dj = dir2vec[direction]
    i2,j2 = i+di, j+dj
    if not (0<=i2<N and 0<=j2<N): # 2. 탈출
        count += 1
        break
    
    if grid[i2][j2] == '#': #1. 정면벽. 회전
        visited[i][j][direction] = True
        direction = (direction+1)%4
        continue
    
    di2,dj2 = dir2vec[(direction-1)%4]
    i3,j3 = i2+di2, j2+dj2
    if grid[i3][j3] == '#': #3. 한칸앞에서 오른쪽벽이있을때. 직진
        visited[i][j][direction] = True
        i,j = i2,j2
        count += 1

    else: #4. 없을때. 우회전.
        visited[i][j][direction] = True
        i,j = i3,j3
        direction = (direction-1)%4
        count += 2




print(count)