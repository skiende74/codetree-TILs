N,M,r,c = map(int, input().split())
directions = input().split()

r,c=r-1,c-1
i,j = r,c
dir2didj = {'L':[0,-1],'R':[0,1],'D':[1,0],'U':[-1,0]}
dir2kl = {'L':lambda k,l: (dices[k][l],l), 'R': lambda k,l: (7-dices[k][l],l),
    'D':lambda k,l: (7-l,k), 'U':lambda k,l: (l,7-k)}

dices = [[0]*7 for _ in range(7)]

dices[1] = [0,0,3,5,2,4,0]
dices[2] = [0,4,0,1,6,0,3]
dices[3] = [0,2,6,0,0,1,5]
dices[4] = [0,5,1,0,0,6,2]
dices[5] = [0,3,0,6,1,0,4]
dices[6] = [0,0,4,2,5,3,0]

grid = [[0]*N for _ in range(N)]
grid[i][j] = 6
k,l = 1,2
for direction in directions:
    di,dj = dir2didj[direction]
    i2,j2 = i+di, j+dj
    if 0<=i2<N and 0<=j2<N:
        fun = dir2kl[direction]
        k,l = fun(k,l)
        grid[i2][j2] = 7-k #stamp
        i,j = i2,j2


total = 0
for i in range(N):
    total += sum(grid[i])
print(total)