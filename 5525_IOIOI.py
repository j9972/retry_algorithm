import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

val = 'I'
for i in range(n):
    val += 'OI'

cnt = 0

for i in range(m-2*n):
    if s[i:i+2*n+1] == val:
        cnt += 1
print(cnt)
