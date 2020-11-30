from collections import defaultdict
class Solution:

    def find_bridges(self, edges):
        bridges = []
        graph = self.build_graph(edges)
        dtime = [float("inf")] * len(graph)
        ltime = [float("inf")] * len(graph)
        visited = [False] * len(graph)
        parent = [-1] * len(graph)

        def find(u, time):
            visited[u] = True
            dtime[u] = time
            ltime[u] = time
            for v in graph[u]:
                if not visited[v]:
                    parent[v] = u
                    find(v, time+1)
                    ltime[u] = min(ltime[u], ltime[v])
                    if ltime[v] > dtime[u]:
                        bridges.append([u, v])
                elif v != parent[u]:
                    ltime[u] = min(dtime[v], ltime[u])

        for v, _ in graph.items():
            if not visited[v]:
                find(v, 0)

        return bridges

    @staticmethod
    def build_graph(edges):
        g = defaultdict(list)
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        return g


if __name__ == '__main__':
    s = Solution()
    edges = [[0,1], [0,2], [2,1],[1,6], [1,3], [1,4], [3,5], [4,5]]
    print(s.find_bridges(edges))