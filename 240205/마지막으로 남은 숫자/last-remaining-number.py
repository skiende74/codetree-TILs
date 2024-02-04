from heapq import heappush, heappop, heapify

N = int(input())
pq = list(map(int,input().split()))

pq = list(map(lambda x: -x, pq))
heapify(pq)

while len(pq)>=2:
    n1 = heappop(pq)
    n2 = heappop(pq)
    d = n2-n1
    if d != 0:
        heappush(pq, -d)

    if len(pq) == 0:
        print(-1)
    elif len(pq) == 1:
        print(-pq[0])