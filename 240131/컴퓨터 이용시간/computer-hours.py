from heapq import heappush, heappop,heapify

N = int(input())
segments = [list(map(int,input().split())) for _ in range(N)]
computers = list(range(1,N+1))
#heapify(computers)

points= []
for index,(s,e) in enumerate(segments):
    points.append((s,1,index))
    points.append((e,-1,index))
points.sort()

ans = [0]*(N)



for x,v,person_idx in points:
    if v==1:
        computer_idx = heappop(computers)
        ans[person_idx] = computer_idx
    else:
        heappush(computers, ans[person_idx])


print(' '.join(map(str, ans)))