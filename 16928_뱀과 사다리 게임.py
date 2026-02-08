import sys
input = sys.stdin.readline
from collections import deque

arr = [i for i in range(101)]

n,m = map(int,input().split())
for i in range(n+m):
    x,y = map(int,input().split())

    arr[x] = y

q = deque()
q.append((1,0))

visited = [False] * 101
visited[1] = True

while q:
    cur_site, cur_cnt = q.popleft()

    if cur_site == 100:
        print(cur_cnt)
        break

    for dice in range(1,7):
        next = dice + cur_site

        if next > 100:
            continue

        next = arr[next]

        if not visited[next]:
            visited[next] = True
            q.append((next, cur_cnt + 1))


    