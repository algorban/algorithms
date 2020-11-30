def path_exists(start, end, maze):
    R, C = len(maze), len(maze[0])
    visited = set()

    def neighbors(node):
        r, c = node
        res = []
        if r + 1 < R and maze[r+1][c] == 0:
            res.append((r+1, c))
        if c + 1 < C and maze[r][c+1] == 0:
            res.append((r, c+1))
        if -1 < r-1 and maze[r-1][c] == 0:
            res.append((r-1, c))
        if -1 < c-1 and maze[r][c-1] == 0:
            res.append((r, c-1))
        return res

    def dfs(node, target):
        if node == target:
            return True
        for next_node in neighbors(node):
            if next_node not in visited:
                visited.add(node)
                result = dfs(next_node, target)
                if result:
                    return True
                visited.remove(node)
        return False

    return dfs(start, end)


maze = [
    [0,0,0,0,1,0],
    [1,1,1,0,1,1],
    [0,0,0,0,0,0],
    [0,1,1,1,1,0],
    [0,0,0,1,0,0]
]
print(path_exists((0,0),(4,0),maze))
