import sys
# 입력
N, M = map(int, input().split())
clothes = [tuple(map(int, input().split())) for _ in range(N)]
clothes.sort()
clothes = [0] + clothes

MIN = -sys.maxsize
dp = [[MIN]*(N+1) for _ in range(M+1)]
dp[0] = [0]*(N+1)


# 본문
values_diff = [[0]*(N+1)]+[[0]+[abs(clothes[i][2]-clothes[j][2]) for j in range(1,N+1)] for i in range(1, N+1)]

for i in range(1,M+1): # 날짜
    for j in range(1,N+1): # 옷
        if clothes[j][0]<=i<=clothes[j][1]:
            dp_next = [0]*(N+1)
            for k in range(1, N+1):
                if clothes[k][0]<=i-1<=clothes[k][1]:
                    dp_next[k] = dp[i-1][k] + values_diff[k][j]
            dp[i][j] = max(dp_next)

print(max(dp[M]))