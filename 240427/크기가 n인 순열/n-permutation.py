from itertools import permutations
N = int(input())
for i,j,k in permutations(range(1,N+1),N):
    print(i,j,k)