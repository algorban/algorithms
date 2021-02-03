import heapq as hq
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
        """
        :type events: List[List[int]]
        :rtype: int
        """
        if len(events) < 2:
            return len(events)
        events.sort()
        total_days = max([day[1] for day in events])

        day, attended, event_id = 1, 0, 0
        min_heap = []
        while day <= total_days:

            # if there are no events in backlog, skip to the nearest start date
            if event_id < len(events) and not min_heap:
                day = events[event_id][0]

            # pushing into backlog events with start date <= day
            while event_id < len(events) and events[event_id][0] <= day:
                hq.heappush(min_heap, events[event_id][1])
                event_id += 1

            # discard events that already ended
            while min_heap and min_heap[0] < day:
                hq.heappop(min_heap)

            # attend event with the earliest end date
            if min_heap:
                hq.heappop(min_heap)
                attended += 1

            day += 1

        return attended


if __name__ == '__main__':
    events =  [[1,1],[4,4],[2,2],[3,4],[1,4]]
    s = Solution()
    print(s.maxEvents(events))

