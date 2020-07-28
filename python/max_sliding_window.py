import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = collections.deque()
        window = collections.deque()
        res = []
        for i, n in enumerate(nums):
            if len(window) == k:
                window.popleft()
            window.append(n)
            print("i = {}, curr element = {}, d = {} and out = {}".format(i, n, d, res))
            while d and nums[d[-1]] < n:
                d.pop()
                print("\t Popped from d because d has elements and nums[d.top] < curr element")
            d.append(i)
            print("\t Added index {} to d".format(i))
            if d[0] == i - k:
                d.popleft()
                print("\t Popped left from d because it's outside the window's leftmost (i-k)")
            if i >= k-1:
                res.append(nums[d[0]])
                print("\t Append nums[d[0]] = {} to out".format(nums[d[0]]))
        return res


if __name__ == '__main__':
    s = Solution()
    array, k = [1,3,-1,-3,5,3,6,7], 3
    print(s.maxSlidingWindow(array, k))


