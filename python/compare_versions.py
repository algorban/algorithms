class Solution:
    """
    Leetcode 165
    Compare two version numbers version1 and version2.
    If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
    You may assume that the version strings are non-empty and contain only digits and the . character.
    The . character does not represent a decimal point and is used to separate number sequences.
    For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision
    of the second first-level revision.
    You may assume the default revision number for each level of a version number to be 0. For example, version number
    3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level
    revision number are both 0.
    """
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split(".")
        ver2 = version2.split(".")

        for v1, v2 in zip(ver1, ver2):
            if int(v1) > int(v2):
                return 1
            elif int(v1) < int(v2):
                return -1

        if len(ver1) == len(ver2):
            return 0

        l = min(len(ver1), len(ver2))
        if len(ver1) > len(ver2):
            for i in range(l, len(ver1)):
                if int(ver1[i]) != 0:
                    return 1
            return 0
        if len(ver2) > len(ver1):
            for i in range(l, len(ver2)):
                if int(ver2[i]) != 0:
                    return -1
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.compareVersion("1.2.1", "1.2.0.5"))