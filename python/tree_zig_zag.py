from collections import deque

class Node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    __repr__ = __str__

class Solution:
    """
    print zig zag binary tree
    """
    def zigzag(self, tree):
        q = deque([tree])
        level = 1
        while q:
            level_size = len(q)
            next_level_q = deque()
            for _ in range(level_size):
                if level % 2 == 0:
                    node = q.popleft()
                    print(node.data, end=' ')
                    if node.left:
                        next_level_q.append(node.left)
                    if node.right:
                        next_level_q.append(node.right)
                else:
                    node = q.pop()
                    print(node.data, end=' ')
                    if node.right:
                        next_level_q.appendleft(node.right)
                    if node.left:
                        next_level_q.appendleft(node.left)
            q = next_level_q
            level += 1
            print()


if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.left.left.left = Node(8)
    tree.left.left.right = Node(9)
    tree.left.right.left = Node(10)
    tree.left.right.right = Node(11)
    tree.right.left.left = Node(12)
    tree.right.left.right = Node(13)
    tree.right.right.left = Node(14)
    tree.right.right.right = Node(15)

    s = Solution()
    s.zigzag(tree)
