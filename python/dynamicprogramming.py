def _lcs(seq1, seq2):
    """
    :param seq1: sequence of symbols (array, list)
    :param seq2: sequence of symbols (array, list)
    :return: int matrix lcs[i][j]
    """
    lcs = [[0 for j in range(0, len(seq2)+1)] for i in range(0, len(seq1)+1)]
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            if seq1[i-1] == seq2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
    return lcs


def lcs(seq1, seq2):
    """
    :param seq1: sequence of symbols (array, list)
    :param seq2: sequence of symbols (array, list)
    :return: longest common subsequence (list)
    """
    subseq = []
    lcs = _lcs(seq1, seq2)
    i = len(lcs)-1
    j = len(lcs[0])-1
    while i>1 or j>1:
        if lcs[i][j]-1 == lcs[i-1][j-1]:
            subseq.append(seq1[i-1])
            i -= 1
            j -= 1
        else:
            if lcs[i-1][j] == lcs[i][j]:
                i -= 1
            else:
                j -= 1
    return list(reversed(subseq))


def coinchange(coins, amount):
    """
    :param coins: list of coins denominations
    :param amount: amount to change
    :return: number of ways of change for given amount
    """
    coins = sorted(coins)
    am = [[0 for j in range(0, amount+1)] for i in range(0, len(coins)+1)]
    for i in range(0, len(coins)+1):
        for j in range(0, amount+1):
            if j == 0:
                am[i][j] = 1
            elif i == 0:
                am[i][j] = 0
            else:
                if coins[i-1] <= j:
                    am[i][j] = am[i-1][j] + am[i][j - coins[i-1]]
                else:
                    am[i][j] = am[i - 1][j]
    return am[len(coins)][amount]

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
#
# Examples:
# s = 'a', p = 'aa' => False
# s = 'a', p = 'a*' => True
# s = 'ab', p = '.*' => True
# s = 'aab',p = 'c*a*b*' => True


def is_match(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    if p is None and s is None:
        return True
    mp = [[False for j in range(0, len(p) + 1)] for i in range(0, len(s) + 1)]
    mp[0][0] = True
    for j in range(1, len(p) + 1):
        if p[j - 1] == "*":
            mp[0][j] = mp[0][j - 2]
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                mp[i][j] = mp[i - 1][j - 1]
            elif p[j - 1] == '*':
                mp[i][j] = mp[i][j - 2]
                if p[j - 2] == "." or p[j - 2] == s[i - 1]:
                    mp[i][j] = mp[i - 1][j] or mp[i][j]
            else:
                mp[i][j] = False
    return mp[len(s)][len(p)]


def perfect_sum(array, sum):
    """
    :param array: list of numbers
    :param sum: amount
    :return: number of subsets which elements add up to given sum
    """
    array = sorted(array)
    dp = [[0 for j in range(0, sum+1)] for i in range(0, len(array)+1)]

    for i in range(0, len(array)+1):
        dp[i][0] = 1

    for j in range(1, sum+1):
        for i in range(1, len(array)+1):
            if array[i-1] <= j:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-array[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(array)][sum]


if __name__ == '__main__':
    assert len(lcs("abcdgtr", "agybtcydik")) == 4
    print("Longest common subsequence of 'abcdgtr' and 'agybtcydik' is ", end=" ")
    print(lcs("abcdgtr", "agybtcydik"))
    assert coinchange([1,2,3], 5) == 5
    print("Number of ways to make a change for 5 using [1,2,3] coins ", end=" ")
    print(coinchange([1,2,3], 5))
    assert perfect_sum([2,4,6,10], 15) == 0
    assert perfect_sum([1,2,3,4,5], 10) == 3

