import sys
input = sys.stdin.readline

n = int(input())
set_list = set()

for _ in range(n):
    set_list.add(input().strip())

# sorted(set_list)

for v in sorted(set_list, key=lambda x : (len(x), x)):
    print(v)