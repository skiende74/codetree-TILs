N = int(input())
orders = [input().split() for _ in range(N)]

now = 0
segments = []
for l,direction in orders:
    l = int(l)
    if direction == 'L':
        left, right = now - l + 1, now
        now = left
    else:
        left, right = now, now+l-1
        now = right
    segments.append([left, right, direction])

seq = [ {'L':0,'R':0,'color':None} for _ in range(200000+1)] # -100,000~100,000. OFFSET = 100000
OFFSET = 100000
WHITE, BLACK, GRAY = 0, 1, 2
for left, right, direction in segments:
    for i in range(left, right+1):
        seq[i+OFFSET][direction] += 1
        if seq[i+OFFSET]['color'] != GRAY:
            if seq[i+OFFSET]['L'] >= 2 and seq[i+OFFSET]['R'] >= 2:
                new_color = GRAY
            elif direction == 'L':
                new_color = WHITE
            else:
                new_color = BLACK
            seq[i+OFFSET]['color'] = new_color

counter = [0,0,0]
for data in seq:
    if data['color'] != None:
        counter[data['color']] += 1
print(' '.join(map(str, counter)))