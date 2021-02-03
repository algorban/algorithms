from collections import defaultdict
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:

    def longest_path(self, root):
        if not root:
            return 0
        nodemap = defaultdict(int)

        def find_path(node, nodemap):
            if not node:
                return len(nodemap)
            nodemap[node.val] += 1
            max_path = max(find_path(node.left, nodemap), find_path(node.right, nodemap))
            nodemap[node.val] -= 1

            if nodemap[node.val] == 0:
                del nodemap[node.val]

            return max_path
        return find_path(root, nodemap)

if __name__ == '__main__':

    tree = Node(1)
    tree.left = Node(2)
    tree.left.left = Node(1)
    tree.left.right = Node(1)
    tree.right = Node(6)
    tree.right.right = Node(1)
    tree.right.right.right = Node(5)

    s = Solution()
    print(s.longest_path(tree))

