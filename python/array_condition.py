class Solution:
    """
    Given array A and number K,
    find if there is a sub array of length 2K that satisfies condition:
    [a, a+1, a+2, ... a+K-1, b, b+1, b+2, ... b+K-1]
    """
    def exists(self, A, K):
        dp = [0] * len(A)

        valid_diff = 1
        for i in range(1, len(A)):
            if A[i] == A[i-1] + valid_diff:
                dp[i] = dp[i-1] + valid_diff
            else:
                dp[i] = dp[i-1]
        print(dp)
        for i in range(len(A) - 2*K+1):
            k_idx = i+K
            if dp[k_idx-1] - dp[i] == K-1 and dp[i+2*K-1] - dp[k_idx] == K-1:
                return i
        return -1


if __name__ == '__main__':
    A = [1,2,3,4,5,7,8,9,12]
    s = Solution()
    print(s.exists(A, 3))
