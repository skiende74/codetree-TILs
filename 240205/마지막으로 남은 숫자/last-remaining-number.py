from heapq import heappush, heappop, heapify

N = int(input())
pq = list(map(int,input().split()))

pq = list(map(lambda x: -x, pq))
heapify(pq)

while len(pq)>=2:
    n1 = heappop(pq)
    n2 = heappop(pq)

    if n1 != n2:
        heappush(pq, n1-n2)
print(-pq[0])