import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

max_cnt , left, kind = 0,0,0
temp = [0] * 10

for right in range(n):
    val = n_list[right]

    if temp[val] == 0:
        kind += 1
    temp[val] += 1
        
    while kind > 2:
        left_val = n_list[left]
        temp[left_val] -= 1

        if temp[left_val] == 0:
            kind -= 1
        
        left += 1
    
    max_cnt = max(max_cnt, right - left + 1)

print(max_cnt)
