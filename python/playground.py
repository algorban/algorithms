from common import Graph

import functools
def compare(a,b):
    return a[0] - b[0]
intervals = [[1,3], [8,10], [2,5], [7,8], [3,4]]
intervals.sort(key = functools.cmp_to_key(compare))

print(intervals)
g = Graph.build_digraph(intervals)
print(g)
stocks = [5,8,3,4,9,7,8]
N = len(stocks)
mmin = mmax = stocks[0]
max_profit = 0
for i in range(N):
    mmax = max(mmax, stocks[i])
    max_profit = max(max_profit, stocks[i] - mmin)
    mmin = min(mmin, stocks[i])
print(max_profit)