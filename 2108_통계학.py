import sys
input = sys.stdin.readline

n = int(input())
arr = [
    int(input())
    for _ in range(n)
]
     
avg = round(sum(arr) / n)
mid = sorted(arr)[n//2]
data_range = abs(max(arr) - min(arr))

d = [
    0
    for _ in range(8001)
]

for i in sorted(arr):
    d[i+4000] += 1

max_val = 0
ans = []

for idx in range(8001):
    if d[idx] > max_val:
        max_val = d[idx]
        ans.clear()
        ans.append(idx-4000)
    elif d[idx] != 0 and d[idx] == max_val:
        ans.append(idx-4000)

print(avg)
print(mid)
if len(ans) == 1:
    print(sorted(ans)[0])
else:
    print(sorted(ans)[1])
print(data_range)