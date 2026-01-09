import sys
input = sys.stdin.readline

n , m = map(int,input().split())

m_list = set()
n_list = set()

for i in range(n):
    n_list.add(input().strip())

for i in range(m):
    m_list.add(input().strip())

print(len(n_list&m_list))
for i in sorted(n_list&m_list):
    print(i,end='\n')
