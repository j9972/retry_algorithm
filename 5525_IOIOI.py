import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

cnt = 0
ans = 0
idx = 0

while idx < m - 2:
    if s[idx:idx+3] == 'IOI':
        cnt += 1

        if cnt >= n:
            ans += 1
        
        idx += 2
    else:
        cnt = 0
        idx += 1
print(ans)
