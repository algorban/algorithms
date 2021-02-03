class Solution:
    """
    We are given hours, a list of the number of hours worked per day for a given employee.
    A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
    A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the
    number of non-tiring days.
    Return the length of the longest well-performing interval.

    Input: hours = [9,9,6,0,6,6,9]
    Output: 3
    Explanation: The longest well-performing interval is [9,9,6].
    """
    def longestWPI(self, hours):
        rsum = []
        for h in hours:
            if h > 8:
                if not rsum:
                    rsum.append(1)
                else:
                    rsum.append(rsum[-1] + 1)
            else:
                if not rsum:
                    rsum.append(-1)
                else:
                    rsum.append(rsum[-1] - 1)
        print(rsum)

if __name__ == '__main__':
    s = Solution()
    print(s.longestWPI([9,9,6,0,6,6,9]))