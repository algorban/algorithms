class UnionFind:

    def __init__(self, n):
        self.ids = [i for i in range(n)]
        self.size = [1] * n

    def find(self, i):
        r = i
        while r != self.ids[r]:
            self.ids[r] = self.ids[self.ids[r]]
            r = self.ids[r]
        return r

    def is_connected(self, i, j):
        return self.find(i) == self.find(j)

    def unify(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)
        if self.size[r1] < self.size[r2]:
            self.ids[r1] = self.ids[r2]
            self.size[r2] += self.size[r1]
        else:
            self.ids[r2] = self.ids[r1]
            self.size[r1] += self.size[r2]


if __name__ == '__main__':
    uf = UnionFind(6)
    edges = [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 1]]
    for edge in edges:
        if uf.is_connected(edge[0], edge[1]):
            print(edge)
        else:
            uf.unify(edge[0], edge[1])
