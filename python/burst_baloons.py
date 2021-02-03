class Solution:

    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        cache = {}
        return self._maxCoins(nums, 0, len(nums)-1, cache)

    def _maxCoins(self, nums, start, end, cache):
        if start == end:
            return nums[start]
        if (start, end) in cache:
            return cache[(start, end)]
        coins = 0
        for i in range(start+1, end):
            coins = max(coins, self._maxCoins(nums, start, i, cache) + self._maxCoins(nums, i, end, cache) + nums[start] * nums[i] * nums[end])
        cache[(start, end)] = coins
        return coins



if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,1,5,8]))