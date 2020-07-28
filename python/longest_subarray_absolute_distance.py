from collections import deque
class Solution:
    def longestSubarray(self, nums, limit):
        min_deque, max_deque = deque(), deque()
        l = r = 0
        ans = 0
        res = []
        while r < len(nums):
            while min_deque and nums[r] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[r] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(r)
            max_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                l += 1
                if l > min_deque[0]:
                    min_deque.popleft()
                if l > max_deque[0]:
                    max_deque.popleft()
            if r - l + 1 > ans:
                ans = r - l + 1
                res = [l, r]
            r += 1

        return res

if __name__ == '__main__':
    s = Solution()
    array = [2,4,3,11,8,9,8,10]
    print(s.longestSubarray(array, 3))