class Solution:
    """
    Leetcode 416
    Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two
    subsets such that the sum of elements in both subsets is equal.
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
    """
    def partition(self, nums):
        if not nums or len(nums) < 2:
            return False
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        N2 = sum_ // 2
        dp = [[False for _ in range(N2+1)] for _ in range(len(nums)+1)]
        nums.sort()
        for i in range(len(nums)):
            dp[i][0] = True

        for partial_sum in range(1, N2+1):
            for j in range(1, len(nums)+1):
                if partial_sum < nums[j-1]:
                    dp[j][partial_sum] = dp[j-1][partial_sum]
                else:
                    dp[j][partial_sum] = dp[j-1][partial_sum] or dp[j][partial_sum - nums[j-1]]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,5]
    print(s.partition(nums))