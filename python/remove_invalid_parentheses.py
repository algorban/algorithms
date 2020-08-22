class Solution(object):
    """
    Leetcode 301. Remove Invalid Parentheses

    Remove the minimum number of invalid parentheses in order to make the input string valid.
    Return all possible results.

    Note: The input string may contain letters other than the parentheses ( and ).

    Example 1:

    Input: "()())()"
    Output: ["()()()", "(())()"]
    Example 2:

    Input: "(a)())()"
    Output: ["(a)()()", "(a())()"]
    """
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        stack = []
        l = 0
        letters = ""
        for p in s:
            if p == '(':
                stack.append(p)
            if p == ')' and stack:
                stack.pop()
                l += 2
            if p not in "()":
                letters += p
        extra = len(s) - l - len(letters)
        if extra == len(s) - len(letters):
            return [letters]

        result = []
        cache = set()
        self.remove(s, extra, result, cache)
        return result

    def remove(self, s, d, result, visited):
        if s in visited:
            return
        visited.add(s)
        if d == 0:
            is_valid = self.is_valid(s)
            if is_valid and s not in result:
                result.append(s)
        for i in range(len(s)):
            if s[i] in '()':
                self.remove(s[:i] + s[i + 1:], d - 1, result, visited)

    def is_valid(self, s):
        open = 0
        for p in s:
            if p == '(':
                open += 1
            if p == ')':
                open -= 1
            if open < 0:
                return False
        return open == 0


if __name__ == '__main__':
    s = Solution()
    print(s.removeInvalidParentheses("(()))e())()"))