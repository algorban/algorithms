from collections import defaultdict
class Solution:

    def pathCost(self, edges, values, start, finish):
        graph, cost = self.build_graph(edges, values)

        def dfs(source, target, visited):
            if source == target:
                return 1
            for nmove in graph[source]:
                if nmove in visited: continue
                visited.add(source)
                ncost = dfs(nmove, target, visited)
                if ncost:
                    return ncost * cost[(source, nmove)]
                visited.remove(source)
            return 0
        return dfs(start, finish, set())


    def build_graph(self, edges, values):
        g = defaultdict(list)
        cost = {}
        for i, edge in enumerate(edges):
            g[edge[0]].append(edge[1])
            g[edge[1]].append(edge[0])
            cost[tuple(edge)] = values[i]
        return g, cost


if __name__ == '__main__':
    edges = [[1,2], [1,8], [2,9], [2,4], [2,3], [4,5], [3,6], [6,7]]
    values = [0.5, 0.6, 0.3, 0.2, 0.9, 2, 4, 3]

    s = Solution()
    print(s.pathCost(edges, values, 1, 7))
