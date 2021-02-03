class Solution(object):
    """
    Leetcode 738. Monotone Increasing Digits
    Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing
    digits.

    (Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y
    satisfy x <= y.)

    Example 1:
    Input: N = 10
    Output: 9
    Example 2:
    Input: N = 1234
    Output: 1234
    Example 3:
    Input: N = 332
    Output: 299
    """
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = list(str(N))
        l, idx = len(num), len(num)

        for i in range(l-2, -1, -1):
            if num[i] > num[i+1]:
                idx = i+1
                num[i] = str(int(num[i])-1)
        for i in range(idx, l):
            num[i] = '9'

        return int("".join(num))


if __name__ == '__main__':
    s = Solution()
    print(s.monotoneIncreasingDigits(2223))
