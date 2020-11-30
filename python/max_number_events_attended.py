import heapq
class Solution(object):
    """
    Leetcode 1353. Maximum Number of Events That Can Be Attended

    Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at
    endDayi.
    You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event
    at any time d.
    Return the maximum number of events you can attend.
    Input: events = [[1,2],[2,3],[3,4]]
    Output: 3
    Explanation: You can attend all the three events.
    One way to attend them all is as shown.
    Attend the first event on day 1.
    Attend the second event on day 2.
    Attend the third event on day 3.
    """
    def maxEvents(self, A):
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res


if __name__ == '__main__':
    events =  [[1,1],[4,4],[2,2],[3,4],[1,4]]
    s = Solution()
    print(s.maxEvents(events))

