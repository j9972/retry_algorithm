import sys
input = sys.stdin.readline

import heapq

for tc in range(int(input())):
    heap = []

    for i in range(int(input())):
        ID, value = input().split()

        if ID == 'I':
            heapq.heappush(heap, int(value))
        elif ID == 'D' and len(heap) != 0:
            if int(value) == 1:    
                heapq.nlargest(1, heap)[0]
            elif int(value) == -1:
                heapq.heappop(heap)
        
        print(i , "번째 : ", heap)
                
    
    if len(heap) == 0:
        print("EMPTY")
    else:
        print(max(heap), heapq.heappop(heap))


