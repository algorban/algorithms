def max_score(nums, k):
    left_sum = sum(nums[:k])
    left_stack = nums[:k]
    res = left_sum
    for i in range(k):
        left = left_stack.pop(0)
        right = nums.pop()
        left_sum = left_sum + (right - left)
        max_sum = max(res, left_sum)
    return max_sum

def _max_score(left, right, k, _sum, array):
    if k == 0:
        return _sum
    return max(_max_score(left+1, right, k-1, _sum + array[left], array), _max_score(left, right+1, k-1, _sum + array[len(array) - right - 1], array))



nums = [2,2,3,4,5,6,1]
k = 3
N = len(nums)
print(_max_score(0, 0, k, 0, nums))

dp = [0] * (k+1)
dp[0] = sum(nums[:k])
for i in range(1, k+1):
    dp[i] = dp[i-1] - nums[k-i] + nums[-i]
print(dp)
print(max(dp))

