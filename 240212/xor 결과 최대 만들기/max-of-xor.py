ans = 0
curr = 0

n,m = map(int,input().split())
seq = list(map(int, input().split()))

def find_max_xor(i, j):
    global ans, curr

    if j == m:
        ans = max(ans, curr)
        return
    
    if i == n:
        return
    
    find_max_xor(i+1, j)
    
    old_curr = curr
    curr ^= seq[i]
    find_max_xor(i+1, j+1)
    curr = old_curr

find_max_xor(0,0)
print(ans)