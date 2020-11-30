class Solution:

    def __init__(self, rooms, meetings):
        max_time = max([item for sublist in meetings for item in sublist])
        self.slots = [0] * (max_time + 1)
        for meeting in meetings:
            self.slots[meeting[0]] += 1
            self.slots[meeting[1]] -= 1
        for i in range(1, len(self.slots)):
            self.slots[i] += self.slots[i-1]

    def can_book(self, interval):
        pass


if __name__ == '__main__':
    intervals = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10], [1, 2]]
    s = Solution(1, intervals)
    print(s.slots)
    print(s.can_book([4, 5]))
    print(s.can_book([5, 6]))