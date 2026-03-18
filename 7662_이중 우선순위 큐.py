import sys
input = sys.stdin.readline

import heapq

def isEmpty(numbers):
    for num in numbers:
        if num[1] > 0:
            return False
    return True

for _ in range(int(input())):

    n = int(input())

    max_heap , min_heap = [], []
    numbers = {}

    for i in range(n):
        char , val = input().split()
        val = int(val)

        if char == 'I':

            if val in numbers:
                numbers[val] += 1
            else:
                heapq.heappush(max_heap, -val)
                heapq.heappush(min_heap, val)
                numbers[val] = 1
        
        elif char == 'D':
            if not isEmpty(numbers.items()):
                if val == 1: # 최댓값
                    while -max_heap[0] not in numbers or numbers[-max_heap[0]] < 1:
                        temp = -heapq.heappop(max_heap)
                        if temp in numbers:
                            del(numbers[temp])
                    numbers[-max_heap[0]] -= 1

                else:
                    while min_heap[0] not in numbers or numbers[min_heap[0]] < 1:
                        temp = heapq.heappop(min_heap)
                        if temp in numbers:
                            del(numbers[temp])
                    numbers[min_heap[0]] -= 1
        
    
    if isEmpty(numbers.items()):
        print("EMPTY")
    else:
        while -max_heap[0] not in numbers or numbers[-max_heap[0]] < 1:
            heapq.heappop(max_heap)
        while min_heap[0] not in numbers or numbers[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])


            