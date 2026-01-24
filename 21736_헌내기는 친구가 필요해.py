import sys
input = sys.stdin.readline

from collections import deque

n,m = map(int,input().split())

arr = [
    list(input().rstrip())
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

def range_(x,y):
    if 0 <= x < n and 0<= y < m:
        return True
    return False

# 방향 북 남 동 서
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 사람 만남
def meet(x,y):
    if arr[x][y] == 'P':
        return True
    return False

# 이동 가능 여부 -> 다음 칸을 파라미터로 넘기기
def move(x,y):
    if range_(x,y) and arr[x][y] != 'X' and visited[x][y] != True:
        return True
    return False

tot = 0
q = deque()

for x in range(n):
    for y in range(m):
        if arr[x][y] == 'I':
            q.append([x,y])
            visited[x][y] = True

while q:
    x,y = q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if move(nx,ny):
            visited[nx][ny] = True
            if meet(nx,ny):
                tot += 1
            q.append([nx,ny])

if tot == 0:
    print('TT')
else:
    print(tot)


