class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        stack = []
        for e in s:
            if e in pairs.values():
                stack.append(e)
            else:
                if stack and stack[-1] == pairs[e]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ss = "()[]{}"
    print(s.isValid(ss))