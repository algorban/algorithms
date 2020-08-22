from collections import Counter
class Solution(object):
    """
    1081. Smallest Subsequence of Distinct Characters
    Return the lexicographically smallest subsequence of text that contains all the distinct characters of text exactly once.
    Example 1:
    Input: "cdadabcc"
    Output: "adbc"
    """

    def smallestSubsequence(self, S):
        last = {c: i for i, c in enumerate(S)}
        stack = []
        for i, c in enumerate(S):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)
        return "".join(stack)


if __name__ == '__main__':
    s = Solution()
    print(s.smallestSubsequence("cbacdcbc"))
