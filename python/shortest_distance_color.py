import collections
class Solution:
    def shortestDistanceColor(self, colors, queries):
        n = len(colors)
        dp = {}
        dp[1] = [float("inf")] * n
        dp[2] = [float("inf")] * n
        dp[3] = [float("inf")] * n

        for i in range(n):
            for color in range(1, 4):
                if i == 0:
                    if color == colors[i]:
                        dp[color][i] = 0
                    continue
                if dp[color][i-1] != float("inf"):
                    dp[color][i] = dp[color][i-1] + 1
                if color == colors[i]:
                    dp[color][i] = 0
        for i in range(n-1, -1, -1):
            for color in range(1, 4):
                if i == n-1:
                    if color == colors[i]:
                        dp[color][i] = 0
                    continue
                dp[color][i] = min(dp[color][i], dp[color][i+1] + 1)
        result = []
        for index, color in queries:
            if color not in dp:
                return [-1]
            result.append(dp[color][index])
        return result



if __name__ == '__main__':
    s = Solution()
    colors = [3, 1, 1, 2, 3, 3, 2, 1, 2, 3, 1, 1, 3, 2, 3, 1, 1, 1, 1, 2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 2, 3, 3, 3, 1, 3, 2, 1, 1,
     2, 2, 1, 3, 1, 2, 1, 1, 2, 2, 1, 2]
    queries = [[10, 2], [0, 1], [32, 3], [1, 1], [41, 1], [48, 3], [0, 3], [46, 2], [48, 2], [28, 1], [47, 2], [11, 2], [49, 3],
     [3, 3], [40, 1], [1, 2], [42, 2], [47, 2], [36, 3], [23, 1], [7, 3], [47, 2], [13, 3], [36, 1], [17, 2], [46, 2],
     [38, 2], [0, 1], [38, 3], [36, 3], [33, 1], [11, 3], [39, 2], [10, 2], [44, 3], [5, 1], [36, 3], [44, 3], [38, 1],
     [9, 1], [9, 1], [35, 3], [10, 1], [9, 1], [0, 3], [1, 1], [0, 3], [28, 1], [22, 3], [15, 1]]
    print(s.shortestDistanceColor(colors, queries))