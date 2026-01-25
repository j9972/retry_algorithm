import sys
input = sys.stdin.readline
import heapq

n = int(input())

h = []

for _ in range(n):
    val = int(input())

    if val < 0:
        heapq.heappush(h,(-val, val))
    elif val > 0:
        heapq.heappush(h,(val, val))
    elif val == 0:
        if len(h) == 0:
            print(0)
        else:
            print(heapq.heappop(h)[1])
    
    