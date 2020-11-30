class Solution:
    """
    Median of unsorted array. Quickselect
    """
    def partition(self, left, right, array):
        pivot = array[right]
        i, j = left, left
        while j < right:
            if array[j] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
            j += 1
        array[i], array[right] = array[right], array[i]
        return i

    def find_median(self, array):
        N = len(array)
        start = 0
        end = N - 1
        expected_pivot = (N - 1) // 2
        pivot = self.partition(start, end, array)
        while expected_pivot != pivot:
            if pivot > expected_pivot:
                pivot = self.partition(start, pivot - 1, array)
            else:
                pivot = self.partition(pivot + 1, end, array)
        if N % 2 == 1:
            return array[pivot]
        else:
            return (array[pivot] + min(array[pivot + 1:])) / 2


if __name__ == '__main__':
    ar = [12, 3, 5, 7, 19, 26]
    s = Solution()
    print(s.find_median(ar))
