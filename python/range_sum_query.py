class NumArray(object):
    """
    307. Range Sum Query - Mutable
    Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

    The update(i, val) function modifies nums by updating the element at index i to val.

    Example:
    Given nums = [1, 3, 5]
    sumRange(0, 2) -> 9
    update(1, 2)
    sumRange(0, 2) -> 8
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums)
        self.tree = self._build_tree(nums)
        self.print_tree()

    def print_tree(self):
        print(self.tree)

    @staticmethod
    def _build_tree(nums):
        n = len(nums)
        tree = [0] * (n * 2)
        for i, j in zip(range(n,2*n), range(n)):
            tree[i] = nums[j]
        for i in range(n-1, 0, -1):
            tree[i] = tree[i*2] + tree[i*2 + 1]
        return tree


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        pos = self.N + i
        self.tree[pos] = val
        while pos > 0:
            left = pos
            right = pos
            if pos % 2 == 0:
                right = pos + 1
            else:
                left = pos - 1
            self.tree[pos//2] = self.tree[left] + self.tree[right]
            pos = pos // 2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        l = i + self.N
        r = j + self.N
        sum = 0
        while l <= r:
            if l % 2 == 1:
                sum += self.tree[l]
                l+= 1
            if r % 2 == 0:
                sum += self.tree[r]
                r -= 1
            l = l // 2
            r = r // 2
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
if __name__ == '__main__':
    na = NumArray([2,4,5,7])
    print(na.sumRange(0,2))
    na.update(2, 6)
    na.print_tree()
    #print(na.sumRange(0, 2))