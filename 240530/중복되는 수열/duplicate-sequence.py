N = int(input())
words = [input() for _ in range(N)]

cnt = 0
class TrieNode():

    def __init__(self):
        self.is_end = False
        self.children = [None]*10
    def insert_word(self, s):
        global cnt
        t = self
        for char in s:
            index = int(char)
            if t.children[index] is None:
                t.children[index] = TrieNode()
            t = t.children[index]
        if t.is_end: cnt += 1
        t.is_end = True
root = TrieNode()

for word in words:
    root.insert_word(word)
print(cnt)