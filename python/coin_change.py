class Solution:
    """
    You are given coins of different denominations and a total amount of money. Write a function to compute the
    number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.
    """
    def number_of_ways(self, coins, amount):
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        dp[0][0] = 1 # base case, 0 amount with no coins = 1 way

        for i in range(1, len(coins)+1):
            dp[i][0] = 1
            for current_amount in range(1, amount+1):
                if current_amount >= coins[i-1]:
                    dp[i][current_amount] = dp[i-1][current_amount] + dp[i][current_amount - coins[i-1]]
                else:
                    dp[i][current_amount] = dp[i - 1][current_amount]

        return dp[-1][-1]

    def if_possible(self, coins, amount):
        dp = [[False for _ in range(amount+1)] for _ in range(len(coins)+1)]
        # base case: 0 amount can be make with any coins
        for i in range(len(coins)+1):
            dp[i][0] = True

        for i in range(1, len(coins)+1):
            for partial_amount in range(1, amount+1):
                if partial_amount >= coins[i-1]:
                    dp[i][partial_amount] = dp[i-1][partial_amount] or dp[i][partial_amount - coins[i-1]]
                else:
                    dp[i][partial_amount] = dp[i - 1][partial_amount]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution();

    print(s.number_of_ways([1,2,3], 5))
    print(s.if_possible([4,5],6))