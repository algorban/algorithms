class Solution(object):
    """
    Leetcode 402. Remove K Digits

    Given a non-negative integer num represented as a string, remove k digits from the number so that the new number
    is the smallest possible.

    Note:
    The length of num is less than 10002 and will be ≥ k.
    The given num does not contain any leading zero.
    Example 1:

    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    """
    def __init__(self):
        self.res = float("inf")

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        N, i = len(num), 0
        while i < N:
            while stack and stack[-1] > num[i] and k > 0:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        while stack and k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == "0":
            i += 1

        if not stack:
            return "0"
        return "".join(stack[i:]) if len("".join(stack[i:])) > 0 else "0"


if __name__ == '__main__':
    s = Solution()
    print(s.removeKdigits("9", 1))