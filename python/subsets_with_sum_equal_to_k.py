def count(idx, _sum, N, nums):
    if _sum == 0:
        return 1
    if idx == N:
        return 0
    return count(idx+1,_sum - nums[idx], N, nums) + count(idx+1, _sum, N, nums)

nums = [2,3,7,1,4,5]
k = 7
print(count(0, k,len(nums), nums))
N = len(nums)
dp = [[0 for _ in range(k+1)] for _ in range(N)]

for i in range(N):
    dp[i][0] = 1

for j in range(1, k+1):
    if nums[0] == j:
        dp[0][j] = 1

for i in range(1, N):
    for j in range(1, k+1):
        if nums[i] <= j:
            dp[i][j] = dp[i-1][j - nums[i]] + dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])