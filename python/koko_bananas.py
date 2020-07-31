class Solution:
    """
    Leetcode: Koko eating bananas
    """
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            # if koko can finish with "m" speed,
            # then either speed "m" is the answer or answer is on the left
            if self.can_finish(piles, m, H):
                r = m
            else:
                l = m + 1
        return r

    def can_finish(self, piles, k, H):
        res = 0
        for p in piles:
            res += (p - 1) // k + 1
        return res <= H

if __name__ == '__main__':
    s = Solution()
    piles = [31,11,23,4,20]
    H = 8
    print(s.minEatingSpeed(piles, H))