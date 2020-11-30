class Solution:

    def distance(self, string1, string2):
        R, C = len(string1), len(string2)

        if R == 0: return C
        if C == 0: return R

        dp = [[0 for _ in range(C+1)] for _ in range(R+1)]

        for r in range(R+1):
            for c in range(C+1):
                if r == 0:
                    dp[r][c] = c
                    continue
                if c == 0:
                    dp[r][c] = r
                    continue
                if string1[r-1] == string2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])
        return dp[r][c]


if __name__ == '__main__':
    s = Solution()
    string1 = "abcd"
    string2 = "abc"
    print(s.distance(string1, string2))