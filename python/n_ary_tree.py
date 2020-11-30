class Node:
    def __init__(self, val, n=3):
        self.val = val
        self.children = [None] * n

class TreeSerializer:
    """
        def deserialize(self, s):

            def helper(s, idx):
                start = idx
                while idx < len(s) and s[idx] != ' ':
                    idx += 1
                c = s[start:idx]
                idx += 1
                if c == '#':
                    return None, idx

                root = Node(int(c))
                child, idx = helper(s, idx)
                while child is not None:
                    root.children.append(child)
                    child, idx = helper(s, idx)
                return root, idx

            root, i = helper(s, 0)
            return root
    """

    def serialize(self, tree):
        result = []
        if tree:
            self._serialize(tree, result)
        return " ".join(result)

    def _serialize(self, tree, result):
        if not tree:
            return
        result.append(str(tree.val))
        for child in tree.children:
            self._serialize(child, result)
        result.append("#")

    @staticmethod
    def deserialize2(string):

        def restore(vals):
            val = next(vals)
            if val == "#":
                return None
            node = Node(int(val))
            child = restore(vals)
            while child:
                node.children.append(child)
                child = restore(vals)
            return node

        if string:
            vals = iter(string.split(" "))
            return restore(vals)


    def deserialize(self, string):
        if string:
            _list = string.split(" ")
            tree = self._deserialize(_list)
            return tree

    @staticmethod
    def _deserialize(_list):
        stack = []
        for val in _list:
            if val == "#":
                if stack:
                    child = stack.pop()
                if stack:
                    stack[-1].children.append(child)
            else:
                stack.append(Node(int(val)))
        return child

    @staticmethod
    def build_tree():
        tree = Node(1)
        tree.children[0] = Node(2)
        tree.children[1] = Node(3)
        tree.children[2] = Node(4)
        tree.children[0].children[0] = Node(5)
        tree.children[0].children[1] = Node(6)
        tree.children[2].children[0] = Node(7)
        tree.children[2].children[1] = Node(8)
        tree.children[2].children[1].children[0] = Node(9)
        return tree

    def traverse(self, node):
        if node:
            print(node.val, end=" ")
            for child in node.children:
                if child:
                    self.traverse(child)
        print("#", end=" ")

if __name__ == '__main__':
    ts = TreeSerializer()
    root = ts.build_tree()
    #ts.traverse(root)
    serialized = ts.serialize(root)
    print(serialized)
    new_tree = ts.deserialize(serialized)
    ts.traverse(new_tree)
    print()
    new_tree2 = ts.deserialize2(serialized)
    ts.traverse(new_tree2)



