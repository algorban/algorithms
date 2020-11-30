from collections import deque

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution():
    def delete(self, root, node):
        if root:
            if root == node and root.left is None and root.right is None:
                return None
            q = deque([(root, None)])  # (node, parent)
            while q:
                current_node, parent = q.popleft()
                if current_node.left:
                    q.append((current_node.left, current_node))
                if current_node.right:
                    q.append((current_node.right, current_node))
            node.val = current_node.val
            if parent.right == current_node:
                parent.right = None
            else:
                parent.left = None
        return root

    def traverse(self,root):
        if root:
            q = [root]
            while q:
                n = q.pop(0)
                print(n.val, end="")
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)


if __name__ == '__main__':
    root = Node(1)
    # root.left = Node(2)
    # root.right = Node(3)
    # root.left.left = Node(4)
    # root.left.right = Node(5)
    # root.right.left = Node(6)
    # root.right.right = Node(7)

    s = Solution()
    s.traverse(root)
    print("")
    root1 = s.delete(root, root)
    s.traverse(root1)
