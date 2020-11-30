class Solution:

    def __init__(self, maze):
        self.maze = maze
        self.R = len(maze)
        self.C = len(maze[0])
        self.visited = set()
        self.path = []

    def find_path(self, sr, sc, er, ec):
        self.path.append((sr, sc))
        self.visited.add((sr, sc))
        if sr == er and sc == ec:
            return True
        for nr, nc in self.neighbors(sr,sc):
            if (nr, nc) in self.visited or self.maze[nr][nc] == 1:
                continue
            res = self.find_path(nr, nc, er, ec)
            if res:
                return True
            else:
                self.path.pop()
                self.visited.remove((nr, nc))
        return False


    def neighbors(self, r, c):
        nbs = []
        if r+1 < self.R:
            nbs.append((r+1, c))
        if c+1 < self.C:
            nbs.append((r, c+1))
        if r-1 > -1:
            nbs.append((r-1, c))
        if c-1 > -1:
            nbs.append((r, c-1))
        return nbs

if __name__ == '__main__':
    maze = [
        [0,0,0,1,0,0,0],
        [0,1,0,1,0,1,0],
        [0,0,0,0,0,1,0],
        [1,1,0,1,1,1,0],
        [1,1,0,1,1,1,0]
    ]
    s = Solution(maze)
    if s.find_path(0,0,4,6):
        print(s.path)
    else:
        print("No path exists!")