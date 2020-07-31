from functools import cmp_to_key
class Solution:

    @staticmethod
    def _compare(self, v1, v2):
        v1list = v1.split(".")
        v2list = v2.split(".")
        for a, b in zip(v1list, v2list):
            if a > b:
                return 1
            elif a < b:
                return -1
        return len(v1) - len(v2)

    def sort_versions(self, versions):
        return sorted(versions, key=cmp_to_key(self._compare))


if __name__ == '__main__':
    s = Solution()
    print(s.sort_versions(["1.2.1", "1.1.0", "1.1", "0.5"]))