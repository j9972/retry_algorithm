import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

q = deque()

def in_range(x,y):
    return 0<=x<n and 0<=y<m

new_arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for x in range(n):
    for y in range(m):
        if arr[x][y] == 2:
            q.append((x,y))
            visited[x][y] = True
            

while q:
    x,y = q.popleft()
    
    for i in range(4):
        cnt = 0
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx,ny) and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                new_arr[nx][ny] = new_arr[x][y] + 1
                q.append((nx,ny))
            

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(0, end=' ')
        elif not visited[i][j]:
            print(-1, end=' ')
        else:
            print(new_arr[i][j], end=' ')
    print()

