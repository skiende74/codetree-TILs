N, M = map(int, input().split())

my_dict = {}
for i in range(1,N+1):
    s = input()
    my_dict[i] = s
    my_dict[s] = i
for j in range(M):
    s = input()

    if s.isnumeric():
        print(my_dict[int(s)])
    else:
        print(my_dict[s])