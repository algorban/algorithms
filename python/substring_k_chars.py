from collections import defaultdict


class Solution(object):
    """
    395. Longest Substring with At Least K Repeating Characters
    Input:
    s = "ababbc", k = 2
    Output:
    5
    The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
    """
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s:
            return 0

        def longest(s, k, start, end):
            if end - start + 1 < k:
                return 0
            freq = defaultdict(int)
            for e in s[start:end + 1]:
                freq[e] += 1
            div = min(freq, key=freq.get)
            if freq[div] >= k:
                return end - start + 1
            div_ptr = start
            for e in s[start:end + 1]:
                if e == div:
                    break
                div_ptr += 1
            left = longest(s, k, start, div_ptr - 1)
            right = longest(s, k, div_ptr + 1, end)
            return max(left, right)

        return longest(s, k, 0, len(s) - 1)

    def longestSubstring2(self, s, k):
        if len(s) < k:
            return 0
        freq = defaultdict(int)
        for e in s:
            freq[e] += 1
        div_element = min(freq, key=freq.get)
        if freq[div_element] >= k:
            return len(s)
        div_element_idx = 0
        for e in s:
            if e == div_element:
                break
            div_element_idx += 1
        left = self.longestSubstring(s[:div_element_idx], k)
        right = self.longestSubstring(s[div_element_idx+1:], k)
        return max(left, right)


if __name__ == '__main__':
    s = Solution()
    string = "ababcabaaaadc"
    k = 1
    print(s.longestSubstring(string, k))
    print(s.longestSubstring2(string, k))