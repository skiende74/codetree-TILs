N = int(input())
seq = [ input().split()[1:] for _ in range(N)]

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

def add(word):
    t = root
    for w in word:
        if w not in t.children: t.children[w] = TrieNode()
        t = t.children[w]
    t.is_end = True

depth = -1
def dfs(w, t):
    global depth
    if w: print('-'*2*depth + w)
    for w, c in sorted(t.children.items()):
        depth += 1
        dfs(w, c)
        depth -= 1

root = TrieNode()
for word in seq:
    add(word)

dfs('', root)