class Node:
    __slots__ = ['val', 'left', 'right']

    def __init__(self, val):
        self.val = val
        self.left = self.right = None

class Solution:

    def smallest(self, root, k):
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


if __name__ == '__main__':
    root = Node(4)
    root.left = Node(2)
    root.right = Node(6)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right.left = Node(5)
    root.right.right = Node(7)
    s = Solution()
    print(s.smallest(root, 5))