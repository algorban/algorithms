class Node:
    __slots__ = ['data', 'left', 'right']

    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return str(self.data)

    __repr__ = __str__


def inittree():
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
    return tree


def preorder(tree):
    """
    :param tree: binary tree
    :return: list of elements of tree preorder traversal
    """
    if tree:
        return [tree.data] + preorder(tree.left) + preorder(tree.right)
    else:
        return []

def inorder(tree):
    """
    :param tree: binary tree
    :return: list of elements of tree inorder traversal
    """
    if tree:
        return inorder(tree.left) + [tree.data] + inorder(tree.right)
    else:
        return []

def postorder(tree):
    """
    :param tree: binary tree
    :return: list of elements of tree postorder traversal
    """
    if tree:
        return postorder(tree.left) + postorder(tree.right) + [tree.data]
    else:
        return []

def treelevels(tree):
    """
    :param tree: binary tree
    :return: list of elements of tree levels from left to right
    """
    queue = []
    result = []
    queue.append(tree)
    while len(queue) > 0:
        node = queue.pop(0)
        result.append(node.data)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result

def treespirallevels(tree):
    """
    :param tree: binary tree
    :return: list of elements of tree in spiral(snake) order
    """
    stack1 = []
    stack2 = []
    level = 1
    result = []
    stack1.append(tree)
    while len(stack1)>0 or len(stack2)>0:
        if level%2 == 1:
            node = stack1.pop()
            result.append(node.data)
            if node.right is not None:
                stack2.append(node.right)
            if node.left is not None:
                stack2.append(node.left)
            if len(stack1) == 0:
                level +=1
        else:
            node = stack2.pop()
            result.append(node.data)
            if node.left is not None:
                stack1.append(node.left)
            if node.right is not None:
                stack1.append(node.right)
            if len(stack2) == 0:
                level +=1
    return result

def _leftnodes(tree, nodes = []):
    """
    Utility function hat returns leftmost nodes of binary tree
    :param tree: binary tree
    :return: list of nodes
    """
    if tree:
        if tree.left is not None or tree.right is not None:
            nodes.append(tree.data)
        if tree.left:
            _leftnodes(tree.left, nodes)
        else:
            _leftnodes(tree.right, nodes)

def _rightnodes(tree, nodes = []):
    """
    Utility function hat returns rightmost nodes of binary tree
    :param tree: binary tree
    :return: list of nodes
    """
    if tree:
        if tree.left is not None or tree.right is not None:
            nodes.insert(0, tree.data)
        if tree.right:
            _rightnodes(tree.right, nodes)
        else:
            _rightnodes(tree.left, nodes)

def _leafnodes(tree, nodes = []):
    """
    Utility function hat returns leaf nodes of binary tree
    :param tree: binary tree
    :return: list of nodes
    """
    if tree:
        if tree.left is None and tree.right is None:
            nodes.append(tree.data)
        _leafnodes(tree.left, nodes)
        _leafnodes(tree.right, nodes)

def treeboundaries(tree):
    """
    :param tree: binary tree
    :return: list of tree boundary elements (anticlockwise)
    """
    left = []
    right = []
    leaves = []
    _leftnodes(tree,left)
    _leafnodes(tree, leaves)
    _rightnodes(tree, right)
    del(right[-1])
    return left + leaves + right

def createtree(preorder, inorder):
    """
    Creates Tree from given Inorder and Preorder traversals
    :param preorder: list of preorder traversal
    :param inorder: list of inorder traversal
    :return: tree
    """
    if len(inorder) > 0:
        element = preorder.pop(0)
        index = inorder.index(element)
        node = Node(element)
        node.left = createtree(preorder, inorder[:index])
        node.right = createtree(preorder, inorder[index+1:])
        return node
    else:
        return None

def findpath(tree, element):
    """
    :param tree: binary tree
    :param element: int (tree node element value)
    :return: path (list of elements) from root to the given node
    """
    if tree:
        if tree.data == element:
            return [element]
        leftlist = findpath(tree.left, element)
        rightlist = findpath(tree.right, element)
        if len(leftlist) > 0:
            return [tree.data] + leftlist
        if len(rightlist) > 0:
            return [tree.data] + rightlist
    return []

def pathbetweennodes(tree, start, end):
    """
    :param tree: binary tree
    :param start: int start node
    :param end: int end node
    :return: path(list of elements) between {start} and {end} nodes
    """
    pathtostart = findpath(tree, start)
    pathtoend = findpath(tree, end)
    idx = 0
    while pathtostart[idx] == pathtoend[idx]:
        idx += 1

    return list(reversed(pathtostart[idx-1:])) + pathtoend[idx:]


def _diameterh(tree):
    if tree is None:
        return 0, 0
    ld, lh = _diameterh(tree.left)
    rd, rh = _diameterh(tree.right)
    return max(lh + rh + 1, ld, rd ), max(lh, rh) + 1


def diameter(tree):
    d, _ = _diameterh(tree)
    return d


def tree2dls(node, next=None):
    """
    :param node: node of binary tree
    :param next: next element(tail)
    :return: head to doubly linked list(inorder traversal)
    """
    if node is None:
        return next
    node.right = tree2dls(node.right, next);
    if node.right:
        node.right.left = node
    return tree2dls(node.left, node)


def tree2dlsi(node):
    """
    :param node: pointer to the binary tree root
    :return: pointer to the doubly linked list(inorder traversal)
    """
    head = None
    stack = []
    done = 0
    current = node
    while not done:
        if current is not None:
            stack.append(current)
            current = current.right
        else:
            if len(stack) > 0:
                current = stack.pop()
                if head is None:
                    head = current
                else:
                    current.right = head
                    head.left = current
                    head = current
                current = current.left
            else:
                done = 1
    return head


if __name__ == '__main__':
    tree = inittree()
    print("Preorder traversal", end=" ")
    print(preorder(tree))
    print("Inorder traversal", end=" ")
    print(inorder(tree))
    print("Postorder traversal", end=" ")
    print(postorder(tree))
    print("Level traversal", end=" ")
    print(treelevels(tree))
    print("Snake(spiral) traversal", end=" ")
    print(treespirallevels(tree))

    prelist = preorder(tree)
    inlist = inorder(tree)
    newtree = createtree(prelist, inlist)
    newprelist = preorder(newtree)
    newinlist = inorder(newtree)
    print("New preorder", end=" ")
    print(newprelist)
    print("New inorder", end=" ")
    print(newinlist)
    prelist = preorder(tree)
    assert ''.join(str(e) for e in prelist) == ''.join(str(e) for e in newprelist)
    assert ''.join(str(e) for e in inlist) == ''.join(str(e) for e in newinlist)

    print("Path to element 11 from root", end=" ")
    print(findpath(tree, 11))

    print("Path between 8 and 11", end=" ")
    print(pathbetweennodes(tree, 8, 11))

    print("Tree boundaries anticlockwise ", end=" ")
    print(treeboundaries(tree))

    print("Diameter of the tree", end=" ")
    print(diameter(tree))
    assert 7 == diameter(tree)

    head = tree2dls(tree)

    print("DLS: ", end=" ")
    while head:
        print(head, end=" ")
        head = head.right
    print()

    tree = inittree()
    head = tree2dlsi(tree)
    print("DLS: ", end=" ")
    while head:
        print(head, end=" ")
        head = head.right
