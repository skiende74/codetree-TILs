N = int(input())

res = 0
def add(x): 
    global res
    res = (1 << x) | res
def delete(x): 
    global res
    if res >> x & 1 == 1:
        res ^= (1 << x)
def print_(x):
    print(1 if (1 << x) & res else 0)
def toggle(x): 
    global res
    res ^= (1 << x)
def clear(): 
    global res
    res = 0
for _ in range(N):
    op, *num = input().split()
    if num: num = int(num[0])
    if op == 'add': add(num)
    elif op == 'delete': delete(num)
    elif op == 'print': print_(num)
    elif op == 'toggle': toggle(num)
    else: clear()