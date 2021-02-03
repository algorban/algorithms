from collections import defaultdict
class Solution:
    """
    Given two strings s and t, return the minimum window in s which will contain all the characters in t.
    If there is no such window in s that covers all characters in t, return the empty string "".

    Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    """
    def minimum_window(self, s, t):
        if not s or not t:
            return 0
        mmap = defaultdict(int)
        for c in t:
            mmap[c] += 1
        min_len = float("inf")
        ans = ""
        for i in range(len(s)):
            map = mmap.copy()
            require = len(t)
            for j in range(i, len(s)):
                c = s[j]
                if c in map and map[c] > 0:
                    map[c] -= 1
                    require -= 1
                if require == 0:
                    local_len = j - i
                    if local_len < min_len:
                        min_len = local_len
                        ans = s[i:j+1]
        return ans


    def min_window(self, s, t):

        if not s or not t:
            return 0
        map = defaultdict(int)
        for c in t:
            map[c] += 1
        require = len(t)
        start, end, min_len, ans = 0, 0, float("inf"), ""

        for end in range(len(s)):
            c = s[end]
            if map[c] > 0:
                require -= 1
            map[c] -= 1
            end += 1
            while require == 0:
                if min_len > end - start:
                    ans = s[start:end]
                    min_len = end - start
                c = s[start]
                map[c] += 1
                if map[c] > 0:
                    require += 1
                start += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.min_window("ADOBECODEABANCDA", "ABC"))
    print(s.minimum_window("ADOBECODEABANCDA", "ABC"))

