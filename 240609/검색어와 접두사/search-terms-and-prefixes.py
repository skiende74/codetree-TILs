class Trie:
    def __init__(self):
        self.children ={}
        self.is_end = False
        self.count = 0

def add(word):
    t = root
    for w in word:
        if w not in t.children: t.children[w] = Trie()
        t = t.children[w]
        t.count += 1
    t.is_end= True

root = Trie()
def search(word):
    t = root
    res = []
    for i, w in enumerate(word):
        if w not in t.children:
            res.extend([0]*(len(word)-i))
            break
        t = t.children[w]
        res.append(t.count)
    return res

N, M = map(int,input().split())
words = input().split()
for word in words:
    add(word)
print(' '.join(map(str, search(input()))))