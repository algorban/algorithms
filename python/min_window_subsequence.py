class Solution:
    """
    Given strings S and T, find the minimum (contiguous) substring W of S, so that T is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty string "". If there are multiple such
minimum-length windows, return the one with the left-most starting index.
    Input:
    S = "abcdebdde", T = "bde"
    Output: "bcde"
    Explanation:
    "bcde" is the answer because it occurs before "bdde" which has the same length.
    "deb" is not a smaller window because the elements of T in the window must occur in order.
    """
    def min_subsequence(self, S, T):
        ans = ""
        for i in range(len(S)):
            if S[i] != T[0]:
                continue
            tindex = 0
            sindex = i
            while tindex < len(T) and sindex < len(S):
                if S[sindex] == T[tindex]:
                    tindex += 1
                    sindex += 1
                else:
                    sindex += 1
            if tindex == len(T):
                if ans == "":
                    ans = S[i:sindex]
                elif len(S[i:sindex]) < len(ans):
                    ans = S[i:sindex]
        return ans

    def min_subsequence_optimized(self, S, T):
        _min = len(S) + 1
        ans = ""
        j = 0
        i = 0
        print(len(S))
        while i < len(S):
            if S[i] == T[j]:
                j += 1
                if j == len(T):
                    end = i + 1
                    j -= 1
                    while j >= 0:
                        if S[i] == T[j]: j -= 1
                        i -= 1
                    j += 1
                    i += 1
                    if end - i < _min:
                        print(i, end)
                        _min = end - i
                        ans = S[i:end]
            i += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    #print(s.min_subsequence("abcdebdde", "bde"))
    print(s.min_subsequence_optimized("ffynmlzesdshlvugsigobutgaetsnjlizvqjdpccdylclqcbghhixpjihximvhapymfkjxyyxfwvsfyctmhwmfjyjidnfryiyajmtakisaxwglwpqaxaicuprrvxybzdxunypzofhpclqiybgniqzsdeqwrdsfjyfkgmejxfqjkmukvgygafwokeoeglanevavyrpduigitmrimtaslzboauwbluvlfqquocxrzrbvvplsivujojscytmeyjolvvyzwizpuhejsdzkfwgqdbwinkxqypaphktonqwwanapouqyjdbptqfowhemsnsl","ntimcimzah"))






