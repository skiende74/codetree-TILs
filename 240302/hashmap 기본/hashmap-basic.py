N = int(input())

my_dict = {}
for _ in range(N):
    x = input().split()

    if x[0] == 'add':
        my_dict[x[1]] = x[2]
    elif x[0] == 'find':
        print(my_dict[x[1]] if x[1] in my_dict else 'None')
    elif x[0] == 'remove':
        del my_dict[x[1]]