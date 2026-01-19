import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

uniq = sorted(set(arr))

dic = dict()
for idx, val in enumerate(uniq):
    dic[val] = idx # 결국 현재 값보다 작은게 몇개냐를 알기위함 으로 dic 사용

for x in arr:
    print(dic[x], end=' ') 
print()

# res = []

# for i in arr:
#     cnt = 0
#     for val in uniq:
#         if i > val:
#             cnt += val
#     res.append(cnt)

# for i in res:
#     print(i, end=' ')