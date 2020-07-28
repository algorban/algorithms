class _Node(object):
    __slots__ = ['char', 'children', 'is_word']

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False


class WordDictionary(object):
    """
    Design a data structure that supports the following two operations:
    void addWord(word)
    bool search(word)
    search(word) can search a literal word or a regular expression string
    containing only letters a-z or ".". A "." means it can represent any one letter.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = _Node("*")

    def insert(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = _Node(char)
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.trie
        return self._search(0, node, word)

    def _search(self, i, node, word):
        if i == len(word):
            return True if node.is_word else False

        char = word[i]
        if char == '.':
            for _, next_node in node.children.items():
                if self._search(i + 1, next_node, word):
                    return True
        else:
            if char not in node.children:
                return False
            else:
                node = node.children[char]
                return self._search(i + 1, node, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


if __name__ == '__main__':
    d = WordDictionary()
    d.insert("hello")
    d.insert("hell")
    d.insert("tree")
    print(d.search("he.lo"))