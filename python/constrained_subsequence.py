from collections import deque
def constrainedSubsetSum(A, k):
    dq = deque()
    R = [0] * len(A)
    for i in range(len(A)):
        R[i] = A[i] + dq[0] if dq else A[i]
        while len(dq) and R[i] > dq[-1]:
            dq.pop()
        if R[i] > 0:
            dq.append(R[i])
        if i >= k and dq and dq[0] == R[i - k]:
            dq.popleft()
    print(A)
    print(R)
    return max(R)

#array = [10,-2,-3,-1, 5, 20]
array = [10,-1,-1,-1,-1,5,5]
k = 2

print(constrainedSubsetSum(array, k))