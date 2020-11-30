class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        R, C = len(matrix), len(matrix[0])
        moves = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        cache = [[0 for _ in range(C)] for _ in range(R)]
        visited = set()

        def dfs(row, col):
            if (row, col) in visited:
                return cache[row][col]
            visited.add((row, col))
            for dr, dc in moves:
                nrow = row + dr
                ncol = col + dc
                if -1 < nrow < R and -1 < ncol < C and matrix[nrow][ncol] > matrix[row][col]:
                    cache[row][col] = max(cache[row][col], dfs(nrow, ncol))
            cache[row][col] += 1
            return cache[row][col]

        ans = 0
        for r in range(R):
            for c in range(C):
                ans = max(ans, dfs(r, c))
        return ans


if __name__ == '__main__':
    s = Solution()
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    print(s.longestIncreasingPath(matrix))