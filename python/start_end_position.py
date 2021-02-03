class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        return [self.find_leftmost(nums, target), self.find_rightmost(nums, target)]

    def find_leftmost(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target and (m == 0 or nums[m - 1] != nums[m]):
                return m
            if target <= nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1

    def find_rightmost(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target and (m == len(nums) - 1 or nums[m + 1] != nums[m]):
                return m

            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if nums[m] == target:
            return m

        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([2,2], 2))