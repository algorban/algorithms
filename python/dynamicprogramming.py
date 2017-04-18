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
                if coins[i-1] <= j :
                    am[i][j] = am[i-1][j] + am[i][j - coins[i-1]]
                else:
                    am[i][j] = am[i - 1][j]
    return am[len(coins)][amount]



if __name__ == '__main__':
    assert len(lcs("abcdgtr", "agybtcydik")) == 4
    print("Longest common subsequence of 'abcdgtr' and 'agybtcydik' is ", end=" ")
    print(lcs("abcdgtr", "agybtcydik"))
    assert coinchange([1,2,3], 5) == 5
    print("Number of ways to make a change for 5 using [1,2,3] coins ", end=" ")
    print(coinchange([1,2,3], 5))
