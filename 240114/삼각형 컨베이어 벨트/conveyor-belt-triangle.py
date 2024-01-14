readList = lambda: list(map(int, input().split()))

n, t = readList()
lines = [readList() for _ in range(3)]


temp0 = lines[0][-1]
for i in range(n-1, 0, -1):
    lines[0][i] = lines[0][i-1]
lines[0][0] = lines[2][-1]


temp1 = lines[1][-1]
for i in range(n-1, 0, -1):
    lines[1][i] = lines[1][i-1]
lines[1][0] = temp0

temp2 = lines[2][-1]
for i in range(n-1, 0, -1):
    lines[2][i] = lines[2][i-1]
lines[2][0] = temp1

for i in range(3):
    print(' '.join(map(str, lines[i])))