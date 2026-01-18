import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())

grand = [
    list(map(int,input().split()))
    for _ in range(n)
]

min_time = 10**9
height = 0

dic = dict()

for i in range(n):
    for j in range(m):
        if grand[i][j] in dic:
            dic[grand[i][j]] += 1
        else:
            dic[grand[i][j]] = 1

for curr_grand_height in range(min(dic), max(dic) + 1):
    add, remove = 0,0

    for h, cnt in dic.items():
        if curr_grand_height > h:
            add += abs(h - curr_grand_height) * cnt
        elif curr_grand_height < h:
            remove += abs(h - curr_grand_height) * cnt
    
    if b + remove >= add:
        time = add + remove * 2
        if min_time > time:
            min_time = time
            height = curr_grand_height

print(min_time, height)
    