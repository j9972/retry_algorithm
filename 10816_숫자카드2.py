import sys
from collections import Counter
input = sys.stdin.readline

# MAX_CNT = 10000000

n = int(input())
n_list = list(map(int,input().split()))

counter = Counter(n_list)

m = int(input())
m_list = list(map(int,input().split()))

print(' '.join(str(counter[i]) for i in m_list))

# arr = [0 for _ in range(MAX_CNT*2+1)]

# for i in n_list:
#     arr[i+MAX_CNT] += 1

# for i in m_list:
#     print(arr[i+MAX_CNT], end=' ')
# print()


