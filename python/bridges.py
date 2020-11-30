def find_bridges(graph):
    disc = {}
    low = {}
    visited = set()
    parent = {}
    bridges = []
    g = graph

    def dfs(v, time):
        visited.add(v)
        disc[v] = time
        low[v] = time
        for n in g[v]:
            parent[n] = v
            if n not in visited:
                dfs(n, time+1)
                low[v] = min(low[n], low[v])
                if low[n] > disc[v]:
                    bridges.append([v, n])
            elif n != parent[v]:
                low[v] = min(low[v], disc[n])
    dfs(0, 0)
    return bridges

graph = {
    0: [1],
    1: [0, 2, 5],
    2: [1, 3],
    3: [2, 4, 5],
    4: [3],
    5: [1, 3]
}

print(find_bridges(graph))