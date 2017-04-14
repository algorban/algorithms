class _Node:
    __slots__ = ['char', 'children', 'is_word', 'word', 'size']

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        self.word = None
        self.size = 0

    def getchild(self, char):
        if char in self.children.keys():
            return self.children[char]
        else:
            return None


class Trie:

    def __init__(self):
        self.trie = _Node("*")

    def insert(self, word):
        currentnode = self.trie
        for char in word:
            nextnode = currentnode.getchild(char)
            if nextnode is None:
                nextnode = _Node(char)
                currentnode.children[char] = nextnode
            nextnode.size += 1
            currentnode = nextnode
        currentnode.is_word = True
        currentnode.word = word



if __name__ == '__main__':
    trie = Trie()
    trie.insert("test")
    print("test")

