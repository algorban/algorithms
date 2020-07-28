from collections import defaultdict, deque

class Solution:

    def frogPosition(self, n, edges, t, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type t: int
        :type target: int
        :rtype: float
        """
        g = self.build_graph(edges)
        q = deque([(1, 0, 1.0)])  # (vertex, hops, probability)
        while q:
            vertex, hops, probability = q.popleft()
            if vertex == target and (hops == t or (hops < t and not g[vertex])):
                return probability
            n = len(g[vertex])
            for _next in g[vertex]:
                q.append((_next, hops + 1, probability * float(1 / n)))
                g[_next].remove(vertex)
        return 0

    @staticmethod
    def build_graph(edges):
        g = defaultdict(set)
        for edge in edges:
            g[edge[0]].add(edge[1])
            g[edge[1]].add(edge[0])
        return g

if __name__ == '__main__':
    edges = [[2, 1]]
    target = 2
    t = 2
    s = Solution()
    print(s.frogPosition(None, edges, t, target))
