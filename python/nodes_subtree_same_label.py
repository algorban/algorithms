import collections
class Solution:
    """
    Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1
    and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a
    lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).
    The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in
    the tree.
    Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same
    label as node i.
    A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
    """
    def countSubTrees(self, n, edges, labels):
        def dfs(node, parent):
            counter = collections.Counter()
            for child in tree[node]:
                if child == parent:
                    continue
                counter += dfs(child, node)
            counter[labels[node]] += 1
            result[node] = counter[labels[node]]
            return counter

        tree = collections.defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        result = [0] * n
        dfs(0, None)
        return result


if __name__ == '__main__':
    s = Solution()
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedbd"
    print(s.countSubTrees(n, edges, labels))