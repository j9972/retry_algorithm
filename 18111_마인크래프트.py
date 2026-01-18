import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())

grand = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_time = 10**9
height = 0

for h in range(min(map(min, grand)), max(map(max, grand)) + 1 ):
    val = 0
    for i in range(n):
        for j in range(m):
            if h > grand[i][j]:
                val += abs(h - grand[i][j])
            elif h < grand[i][j]:
                val += abs(h - grand[i][j]) * 2
    
    if min_time >= val:
        min_time = val
        height = h

print(min_time, height)

            
