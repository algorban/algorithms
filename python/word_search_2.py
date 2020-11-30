"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally
or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""
class Node(object):
    __slots__ = ['char', 'children', 'is_word', 'word']

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_word = False
        self.word = None


class Solution(object):

    @staticmethod
    def add_word(root, word):
        node = root
        for e in word:
            if e not in node.children:
                node.children[e] = Node(e)
            node = node.children[e]
        node.is_word = True
        node.word = word

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        R = len(board)
        C = len(board[0])
        trie = Node("*")
        for word in words:
            self.add_word(trie, word)
        words = set()
        visited = set()

        def dfs(r, c, node):
            if r < 0 or r == R or c < 0 or c == C or (r, c) in visited:
                return
            child = node.children.get(board[r][c], None)
            if child is None:
                return
            if child.is_word:
                words.add(child.word)
            visited.add((r, c))
            dfs(r + 1, c, child)
            dfs(r - 1, c, child)
            dfs(r, c + 1, child)
            dfs(r, c - 1, child)
            visited.remove((r,c))

        for r in range(R):
            for c in range(C):
                visited = set()
                dfs(r, c, trie)
        return words


if __name__ == '__main__':
    s = Solution()
    board = [["a", "b", "c"], ["a", "e", "d"], ["a", "f", "g"]]
    words = ["abcdefg", "gfedcbaaa", "eaabcdgfa", "befa", "dgc", "ade"]
    print(s.findWords(board, words))