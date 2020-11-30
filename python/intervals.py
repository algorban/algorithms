import heapq as hq

intervals =  [[1, 3], [2, 4], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
intervals.sort()
h = []
result = []
for interval in intervals:
    while h and interval[0] >= h[0][1]:
        hq.heappop(h)
    hq.heappush(h, interval)
