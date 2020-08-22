class Node(object):
    def __init__(self, val):
        self.val = val
        self.cnt = 0
        self.left = self.right = None


class Solution(object):
    """
    Leetcode 315.  Count of Smaller Numbers After Self
    You are given an integer array nums and you have to return a new counts array. The counts array has the property
    where counts[i] is the number of smaller elements to the right of nums[i].

    Example 1:

    Input: nums = [5,2,6,1]
    Output: [2,1,1,0]
    Explanation:
    To the right of 5 there are 2 smaller elements (2 and 1).
    To the right of 2 there is only 1 smaller element (1).
    To the right of 6 there is 1 smaller element (1).
    To the right of 1 there is 0 smaller element.
    """
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return None
        res = []
        root = None
        for i in range(len(nums)-1, -1, -1):
            root = self.insert(root, nums[i], 0, res)
        res.reverse()
        return res

    def insert(self, root, val, s, res):
        if root is None:
            res.append(s)
            return Node(val)
        if root.val < val:
            s += root.cnt + 1
            root.right = self.insert(root.right, val, s, res)
        else:
            root.left = self.insert(root.left, val, s, res)
            root.cnt += 1

        return root





if __name__ == '__main__':
    s = Solution()
    """
    tree = s.build_tree([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])
    q = [tree]
    while q:
        node = q.pop(0)
        print(node.val, node.cnt)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    """
    print(s.countSmaller([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]))