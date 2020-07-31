class Solution:
    """
    68 Leetcode

    """
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        length = 0
        buffer = []
        result = []
        for word in words:
            if length + len(word) > maxWidth:
                result.append(self._align(buffer, maxWidth, False))
                buffer, length = [word], len(word) + 1
            else:
                buffer.append(word)
                length = length + len(word) + 1
        if buffer:
            result.append(self._align(buffer, maxWidth, True))
        return result

    def _align(self, words, maxWidth, last=False):
        if last:
            string = " ".join(words)
            string = string + " " * (maxWidth - len(string))
            return string
        else:
            breaks = len(words) - 1
            if breaks == 0:
                return words[0] + " " * (maxWidth - len(words[0]))
            else:
                letters = self._get_total_length(words)
                spaces = maxWidth - letters
                space = spaces // breaks
                leftover = spaces % breaks
                string = ""
                for i, word in enumerate(words):
                    if i == len(words) - 1:
                        string = string + word
                    else:
                        string = string + word + " " * space
                        if leftover > 0:
                            string += " "
                            leftover -= 1
                return string

    @staticmethod
    def _get_total_length(words):
        total = 0
        for word in words:
            total += len(word)
        return total


if __name__ == '__main__':
    s = Solution()
    #words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["Leetcode", "is", "a", "good", "site", "to", "practice", "skills"]
    print (s.fullJustify(words, 8))
