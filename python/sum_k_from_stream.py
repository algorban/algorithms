class Solution:

    @staticmethod
    def sum_k_from_stream(stream, K):
        sums = [False] * (K + 1)
        sums[0] = True

        for element in stream:
            if element > K:
                continue
            for partial_sum in range(K, element - 1, -1):
                sums[partial_sum] = sums[partial_sum - element] or sums[partial_sum]
            if sums[-1]:
                return True
        return False


if __name__ == '__main__':
    s = Solution()
    stream = [2, 5, 2, 6, 8, 3, 9, 4, 7, 2, 3, 2, 6, 9, 8, 4]
    print(s.sum_k_from_stream(stream, 1))
