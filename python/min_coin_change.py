class Solution:
    """
    You are given coins of different denominations and a total amount of money. Write a function to compute the
    number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
    """
    def min_coins(self, coins, amount):
        dp = [[float("inf") for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 0 # base case, 0 amount 0 coins

        for i in range(1, len(coins)+1):
            dp[i][0] = 0
            for current_amount in range(1, amount+1):
                if current_amount >= coins[i-1]:
                    dp[i][current_amount] = min(dp[i-1][current_amount], dp[i][current_amount - coins[i-1]] + 1)
                else:
                    dp[i][current_amount] = dp[i - 1][current_amount]

        return dp[-1][-1]



if __name__ == '__main__':
    s = Solution();

    print(s.min_coins([1, 3, 5], 11))