from collections import Counter
N, Q = map(int,input().split())
parent = [i for i in range(N+1)]
counter = [1]*(N+1)
def union(i,j):
    r1,r2 = find(i), find(j)
    if r1<=r2:
        parent[r2] = r1
        counter[r1] += counter[r2]
    else:
        parent[r1] = r2
        counter[r2] += counter[r1]
def find(i):
    if parent[i] == i: return i
    parent[i] = find(parent[i])
    return parent[i]

search = []
for _ in range(Q):
    query = input().split()
    if query[0] == 'x':
        i, j = map(int,query[1:])
        union(i,j)
    else:
        a = int(query[1])
        print(counter[find(a)])