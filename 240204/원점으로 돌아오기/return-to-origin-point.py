N = int(input())
points = [(0,0)] + [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N+1)]

for i in range(N+1):
    for j in range(i+1, N+1):
        if i != j:
            if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                graph[i].append(j)
                graph[j].append(i)

def dfs(i, direction):
    global answer
    if len(result) == N+2 and result[-1] == start:
        answer += 1
        return
    for j in graph[i]:
        if not visited[j] and not is_same_dir(i,j,direction):
            visited[j] = True
            result.append(j)
            dfs(j, get_direction(points[i], points[j]))
            result.pop()
            visited[j] = False

RIGHT,LEFT, UP, DOWN = 0,1,2,3
def get_direction(point1, point2):
    if point2[0] > point1[0]:
        return RIGHT
    if point2[0] < point1[0]:
        return LEFT
    if point2[1] > point1[1]:
        return UP
    return DOWN

def is_same_dir(i, j, direction):
    direction2 = get_direction(points[i], points[j])
    return direction == direction2
answer = 0
start = 0
result = [0]
visited = [False]*(N+1)
dfs(start, None)
print(answer)