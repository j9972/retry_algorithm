import sys
import heapq
input = sys.stdin.readline

heap = []


n = int(input())

for i in range(n):
    val = int(input())

    if val == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, val)