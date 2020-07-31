import math
class Solution(object):
    """
    279 Perfect squares
    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...)
    which sum to n.
    """
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n

        dp = [float("inf")] * (n + 1)
        dp[0], dp[1], dp[2], dp[3] = 0, 1, 2, 3

        for i in range(4, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                dp[i] = min(dp[i], dp[i - j * j]+1)

        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(13))