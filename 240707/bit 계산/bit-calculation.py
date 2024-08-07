N = int(input())
num = 0
for _ in range(N):
    op, *n = input().split()
    
    if n: n = int(n[0])
    
    if op == 'add':
        num |= 1 << n
    elif op == 'delete' and num & (1 << n):
        num ^= 1 << n
    elif op == 'print':
        print( 1 if num & (1 << n) else 0)
    elif op == 'toggle':
        num ^= 1 << n
    else:
        num = 0