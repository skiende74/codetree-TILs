import sys
N = int(input())
grid = [list(map(int,input().split())) for _ in range(N)]

MAX = sys.maxsize
dp = [[MAX]*N for _ in range(N)]
def initialize_dp():
    for i in range(N):
        for j in range(N):
            dp[i][j] = MAX
    
    dp[0][0] = grid[0][0]
    
    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], grid[i][0])
    for j in range(1, N):
        dp[0][j] = max(dp[0][j-1], grid[0][j])

def solve(MIN):
    for i in range(N):
        for j in range(N):
            if grid[i][j] < MIN:
                grid[i][j] = MAX
        
    initialize_dp()

    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = max(min(dp[i][j-1], dp[i-1][j]), grid[i][j])
    
    return dp[-1][-1]

answer = MAX
for lower_bound in range(1, 100+1):
    upper_bound = solve(lower_bound)

    if upper_bound == MAX: continue
    answer = min(answer, abs(upper_bound - lower_bound))
print(answer)