import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    dic = dict()

    for _ in range(n):
        name, clothes = input().split()

        if clothes not in dic:
            dic[clothes] = 1
        else:
            dic[clothes] += 1
    
    res = 1
    for k, v in dic.items():
        res *= (v + 1)
    
    print(res-1)
