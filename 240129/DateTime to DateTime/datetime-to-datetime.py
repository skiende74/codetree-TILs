a, b, c = list(map(int,input().split()))

result = (a*24*60 + b*60 + c ) - (11*24*60+11*60+11)
print(result if result >= 0 else -1)