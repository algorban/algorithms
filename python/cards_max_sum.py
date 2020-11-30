class Solution:

    def max_sum(self, cards, K):

        def _max_sum(left, right, K, _sum):
            if K == 0:
                return _sum
            return max(_max_sum(left+1, right, K-1, cards[left] + _sum), _max_sum(left, right-1, K-1, cards[right] + _sum))

        return _max_sum(0, len(cards)-1, K, 0)

    def max_sum2(self, cards, K):
        dp = [[0 for _ in range(K+1)] for _ in range(K+1)]
        N = len(cards)
        for i in range(1, K+1):
            dp[0][i] = dp[0][i-1] + cards[N-i]
        for i in range(1, K+1):
            dp[i][0] = dp[i-1][0] + cards[i-1]

        for left in range(1, K+1):
            for right in range(1, K+1-left):
                dp[left][right] = max(dp[left-1][right] + cards[left-1], dp[left][right-1] + cards[N-right])
        _max = 0
        for i in range(K+1):
            _max = max(_max, dp[i][K-i])
        return _max


if __name__ == '__main__':

    s = Solution();

    cards = [1,10,3,4,5,6,7,1,9]
    #s.max_sum2(cards, 2)
    print(s.max_sum(cards, 3))
    print(s.max_sum2(cards, 3))

