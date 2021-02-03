class Node:

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.word = None
        self.is_word = False
        self.rank = 0


class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Node("*")
        self.keyword = ""
        self.populate(sentences, times)

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        c = str(c)
        if c == "#":
            self.insert(self.keyword, 1)
            self.keyword = ""
        else:
            self.keyword += c
            res = self.search(self.keyword)
            res.sort(key=lambda x: (-x[0], x[1]))
            return [r[1] for r in res[:3]]

    def populate(self, sentences, times):
        for i, sentence in enumerate(sentences):
            self.insert(sentence, times[i])

    def insert(self, sentence, rank):
        node = self.trie
        for w in sentence:
            w = str(w)
            next_node = node.children.get(w, None)
            if next_node is None:
                next_node = Node(w)
                node.children[w] = next_node
            node = next_node
        node.word = sentence
        node.rank += rank
        node.is_word = True

    def search(self, keyword):
        result = []
        node = self.trie
        for w in keyword:
            if w not in node.children:
                return result
            node = node.children[w]
        self.dfs(node, result)
        return result

    def dfs(self, node, result):
        if node.is_word:
            result.append((node.rank, node.word))
        for next_node in node.children.values():
            self.dfs(next_node, result)

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

if __name__ == '__main__':
    sentences = ["i love you","island","iroman","i love leetcode"]
    times = [5,3,2,2]
    ac = AutocompleteSystem(sentences,times)
    print(ac.input("i"))
    print(ac.input("#"))
    print(ac.input("i"))