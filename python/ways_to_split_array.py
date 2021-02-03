class Solution:
    """
    A split of an integer array is good if:
    The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
    The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the
    elements in mid is less than or equal to the sum of the elements in right.

    Example:
    Input: nums = [1,2,2,2,5,0]
    Output: 3
    Explanation: There are three good ways of splitting nums:
    [1] [2] [2,2,5,0]
    [1] [2,2] [2,5,0]
    [1,2] [2,2] [5,0]
    """
    def waysToSplit(self, nums):
        prefix = [0]
        for x in nums: prefix.append(prefix[-1] + x)

        ans = j = k = 0
        for i in range(1, len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and 2 * prefix[i] > prefix[j]: j += 1
            k = max(k, j)
            while k < len(nums) and 2 * prefix[k] <= prefix[i] + prefix[-1]: k += 1
            ans += k - j
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.waysToSplit([4,2,3,0,3,5,3,12]))