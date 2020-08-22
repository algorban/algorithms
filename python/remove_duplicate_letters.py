from collections import defaultdict

class Solution(object):
    """
    Leetcode 316
    Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once
    and only once. You must make sure your result is the smallest in lexicographical order among all possible results.
    Example 1:
    Input: "bcabc"
    Output: "abc"
    """
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_index = self.lastIndex(s)
        stack = []
        for i, letter in enumerate(s):
            if letter in stack: continue
            while stack and stack[-1] > letter and i < last_index[stack[-1]]:
                stack.pop()
            stack.append(letter)
        return "".join(stack)


    @staticmethod
    def lastIndex(s):
        last = defaultdict(int)
        for i, letter in enumerate(s):
            last[letter] = i
        return last


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicateLetters("cbacdcbc"))
