import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic = dict()
m_list = []

for i in range(n):
    site, password = input().split()

    dic[site] = password

for i in range(m):
    site = input().strip()
    print(dic[site])

