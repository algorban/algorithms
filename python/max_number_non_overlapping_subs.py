class Solution:
    """
    Leetcode 1520:

    Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet
    the following conditions:

    The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
    A substring that contains a certain character c must also contain all occurrences of c.

    Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same
    number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution
    of minimum total length.

    Notice that you can return the substrings in any order.
    """
    def maxNumOfSubstrings(self, s):
        if not s:
            return []

        chrange = {}
        for i, c in enumerate(s):
            if c not in chrange:
                chrange[c] = [i, i]
            else:
                chrange[c][1] = i

        for c in chrange:
            left, right = chrange[c]
            _l, _r = left, right
            while True:
                for ch in set(s[_l:_r]):
                    _l = min(_l, chrange[ch][0])
                    _r = max(_r, chrange[ch][1])
                if (_l, _r) == (left, right): break
                left, right = _l, _r
            chrange[c] = (_l, _r)

        sorted_ranges = sorted(chrange.values(), key=lambda r: r[1])
        res, prev = [], 0
        for r in sorted_ranges:
            if r[0] >= prev:
                res.append(s[r[0]:r[1]+1])
                prev = r[1]
        return res


if __name__ == '__main__':
    s = Solution()
    string = "adefaddaccc"
    print(s.maxNumOfSubstrings(string))