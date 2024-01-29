N = int(input())
blocks = [int(input()) for _ in range(N)]

avg_block = sum(blocks)//N

ans = 0

def test():
    for b in blocks:
        if b != avg_block:
            return False
    return True

while not test():
    max_block = max(blocks)
    max_idx = blocks.index(max_block)
    min_block = min(blocks)
    min_idx = blocks.index(min_block)

    amount = min(max_block-avg_block, avg_block-min_block)
    blocks[max_idx] -= amount
    blocks[min_idx] += amount
    ans += amount
print(ans)