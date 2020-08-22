import heapq as hq
class Solution(object):
    """
    Leetcode 1296. Divide Array in Sets of K Consecutive Numbers
    Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets
    of k consecutive numbers
    Return True if its possible otherwise return False.
    Example 1:

    Input: nums = [1,2,3,3,4,4,5,6], k = 4
    Output: true
    Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
    """
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False
        nums.sort()
        h = [(nums[0], 1)]

        for n in nums[1:]:
            while h and h[0][1] == k:
                hq.heappop(h)
            if not h:
                hq.heappush(h, (n, 1))
            else:
                if h[0][0] == n or h[0][0] < n - 1:
                    hq.heappush(h, (n, 1))
                elif h[0][0] == n - 1:
                    last, length = hq.heappop(h)
                    hq.heappush(h, (n, length + 1))
                else:
                    return False

        for _, length in h:
            if length != k:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums =  [10, 9, 8, 1, 2, 3, 2, 3, 4, 4, 5, 6, 10, 11, 12]
    k = 3
    print(s.isPossibleDivide(nums,k))