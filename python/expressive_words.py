class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        stretchy = 0

        for word in words:
            if self.is_stretchy(word, S):
                stretchy += 1
        return stretchy

    def is_stretchy(self, word, S):
        if len(word) > len(S):
            return False

        p1, p2 = 0, 0

        while p1 < len(word) and p2 < len(S):
            if word[p1] != S[p2]:
                return False

            char = word[p1]

            c1, c2 = 0, 0

            while p1 < len(word) and word[p1] == char:
                c1 += 1
                p1 += 1

            while p2 < len(S) and S[p2] == char:
                c2 += 1
                p2 += 1

            if c1 > c2 or (c2 < 3 and c1 != c2):
                return False

        if p1 < len(word) or p2 < len(S):
            return False

        return True

if __name__ == '__main__':
    s = Solution()
    S = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(s.expressiveWords(S, words))