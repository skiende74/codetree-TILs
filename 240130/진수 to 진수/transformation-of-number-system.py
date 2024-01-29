a, b = map(int, input().split())
n_a = input()

decimal = 0
for bb in n_a:
    decimal = decimal*a + int(bb)

n_b = ''
while decimal > 0:
    decimal, k = divmod(decimal, b)
    n_b = str(k) + n_b

print(n_b)