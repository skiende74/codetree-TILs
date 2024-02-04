from heapq import heappush, heappop
N = int(input())

pq = []
for _ in range(N):
    n = int(input())
    if n == 0:
        if pq:
            print(-heappop(pq))
        else:
            print(0)
    else:
        heappush(pq, -n)