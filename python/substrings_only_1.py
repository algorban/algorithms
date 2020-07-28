import math
class Solution(object):
    """
    Given a binary string s (a string consisting only of '0' and '1's).
    Return the number of substrings with all characters 1's.
    """
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        current_length = 0
        total = 0
        for n in s:
            if n == '0':
                total = total + (current_length * (current_length + 1))/2
                current_length = 0
            else:
                current_length += 1
        total = total + (current_length * (current_length + 1))/2
        return total


if __name__ == '__main__':
    s = Solution()
    string = "111111" # 5 + 4 + 3 + 2 + 1 # 4 + 3 + 2 + 1
    print(s.numSub(string))