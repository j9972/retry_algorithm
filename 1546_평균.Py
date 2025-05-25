n = int(input())
arr = list(map(int,input().split()))
max_num = max(arr)

new_arr = []
for i in arr:
    new_arr.append(i/max_num*100)

print(sum(new_arr) / n)