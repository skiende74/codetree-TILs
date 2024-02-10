N = int(input())
dscores = [input().split() for _ in range(N)]

score= [0, 0]
max_score = 0
max_idxs = [1,2]

for dscore in dscores:
    person, ds = dscore
    if person == 'A':
        score[0] += ds
    else:
        score[1] += ds