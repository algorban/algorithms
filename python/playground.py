def min_deletions(string):
    """
    We are given a string SS of length NN consisting only of letters A and/or B. Our goal is to obtain a string in the
    format A...AB...B. (all letters A occur before all letters B) by deleting some letters from SS. In particular,
    strings consisting only of letters A or only of letters B fit this format.

    Write a function that, given a string SS, return the minimum number of letters that need to be deleted from SS in
    order to obtain a string in the above format.

    Example:
        Input: "BAAABAB"
        Output: 2
        Explanation: We can obtain "AAABB" by deleting the first occurrence of 'B' and the last occurrence of 'A'.
    """
    min_deletions, left_b = 0, 0
    if not string:
        return min_deletions

    for e in string:
        if e == 'A':
            min_deletions = min(left_b, min_deletions + 1)
        else:
            left_b += 1

    return min_deletions

#s = "BBABAA"
#print(min_deletions(s))


def binary_concat(number):
    result = 0
    shift = 0
    while number > 0:
        tmp = number
        tmp = tmp << shift
        result = tmp | result
        tmp = number
        while tmp > 0:
            tmp = tmp >> 1
            shift += 1
        number -= 1
    return result

print(binary_concat(3))


def digits_sum(n):
    _sum = 0
    while n > 0:
        _sum += n % 10
        n = n // 10
    return _sum

print(digits_sum(92))