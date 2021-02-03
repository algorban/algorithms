class _Node:
    __slots__ = ['char', 'children', 'is_word', 'word', 'size']

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        self.word = None
        self.size = 0

    def get_child(self, char):
        if char in self.children.keys():
            return self.children[char]
        else:
            return None


class Trie:

    def __init__(self):
        self.trie = _Node("*")

    def insert(self, word):
        current_node = self.trie
        for char in word:
            next_node = current_node.get_child(char)
            if next_node is None:
                next_node = _Node(char)
                current_node.children[char] = next_node
            next_node.size += 1
            current_node = next_node
        current_node.is_word = True
        current_node.word = word


if __name__ == '__main__':
    trie = Trie()
    trie.insert("test")
    trie.insert("letter")
    trie.insert("leet")
    trie.insert("leetcode")
    print("")

