# 입력
readList = lambda: list(map(int, input().split()))
n, t = readList()
line1 = readList()
line2 = readList()

# 본문
def move():
    temp = line1[n-1]
    for i in range(n-1, 0, -1):
        line1[i] = line1[i-1]

    line1[0] = line2[n-1]
    for i in range(n-1, 0, -1):
        line2[i] = line2[i-1]

    line2[0] = temp


for _ in range(t):
    move()
print(' '.join(map(str, line1)))
print(' '.join(map(str, line2)))