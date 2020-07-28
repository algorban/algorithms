class Solution:
    """
    Return k-th missing number in the given sorted array
    """
    def kth_number(self, nums, K):
        diff = nums[-1] - nums[0]
        N = len(nums)
        missing = diff - N + 1
        if K > missing:
            return nums[-1] + (K - missing)
        left, right = 0, len(nums)-1

        while left+1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing >= K:
                right = mid
            else:
                left = mid
                K -= missing
        return nums[left] + K


if __name__ == '__main__':
    s = Solution()
    nums = [2,3,5,8,9,10,11,13,18] # missing = [4,6,7,12,14,15,16,17,]
    #nums = [1,3]
    print(s.kth_number(nums,12))