class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        N = len(nums)
        subsets = []
        for i in range(N):
            subsets.append([nums[i]])

        for i in range(1, N):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(subsets[j]) >= len(subsets[i]):
                    subsets[i] = subsets[j] + [nums[i]]
        res = []
        for i in range(N):
            if len(subsets[i]) > len(res):
                res = subsets[i]
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,4,8,9,16]
    print(s.largestDivisibleSubset(nums))
