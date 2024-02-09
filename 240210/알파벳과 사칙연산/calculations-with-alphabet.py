import sys
sys.setrecursionlimit(100000)
def get_num(char):
    return selected_nums[ord(char) - ord('a')]
def dfs():
    global ans
    if len(selected_nums) == 6:
        ans = max(ans, calc())
        return

    for j in range(1,5):
        selected_nums.append(j)
        dfs()
        selected_nums.pop()

def calc():
    result = get_num(alphas[0])
    for alpha, op in zip(alphas[1:], ops):
        if op == '+':
            result *= get_num(alpha)
        if op == '-':
            result -= get_num(alpha)
        if op == '*':
            result *= get_num(alpha)
        if op == '/':
            result /= get_num(alpha)
    return result

eq = input()
selected_nums = []
alphas, ops = [eq[0]] , []
for i in range(1, len(eq)):
    if i%2 == 1:
        ops.append(eq[i])
    else:
        alphas.append(eq[i])
N = len(ops)
ans = -2**31
dfs()
print(ans)