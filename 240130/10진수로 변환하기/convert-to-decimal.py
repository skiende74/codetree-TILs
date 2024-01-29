binary = input()

ans = 0
for b in binary:
    ans = ans*2 + int(b)

print(ans)