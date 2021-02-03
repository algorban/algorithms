class Solution:

    def min_steps(self, piles):
        piles.sort()
        N = len(piles)
        if N < 2:
            return 0
        steps = 0
        for i in range(1, N):
            if piles[N-i-1] != piles[N-i]:
                steps += i
        return steps


if __name__ == '__main__':

    s = Solution()
    print(s.min_steps([1,2,2,2,2,2]))