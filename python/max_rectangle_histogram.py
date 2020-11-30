class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]

        stack = [-1]
        maxArea = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                lastIndex = stack.pop()
                maxArea = max(maxArea, heights[lastIndex] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            lastIndex = stack.pop()
            maxArea = max(maxArea, heights[lastIndex] * (len(heights) - stack[-1] - 1))
        return maxArea



if __name__ == '__main__':
    s = Solution()
    nums = [2,2,2,2,2,2,2]
    print(s.largestRectangleArea(nums))