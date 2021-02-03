class Node:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        self.word = None


class Solution:

    def __init__(self, words):
        self.trie = self.build_trie(words)

    @staticmethod
    def build_trie(words):
        trie = Node("*")
        for word in words:
            node = trie
            for w in word:
                if node.children.get(w, None) is None:
                    node.children[w] = Node(w)
                node = node.children[w]
            node.is_word = True
            node.word = word
        return trie

    def find_words(self, number):
        words = []
        n2w = {"0": "", "1": "", "2":"abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        def dfs(node, number, idx):
            if len(number) == idx:
                if node.is_word:
                    words.append(node.word)
                return
            for w in n2w[number[idx]]:
                if node.children.get(w, None):
                    dfs(node.children[w], number, idx+1)
        dfs(self.trie, number, 0)
        return words


if __name__ == '__main__':
    words = ["hello", "name", "phone", "hi", "gdjkm", "hellp"]
    s = Solution(words)
    print(s.find_words("43556"))
