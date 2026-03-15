from collections import deque

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10


def D(number):
    return (number * 2) % 10000

def S(number):
    return number - 1 if number != 0 else 9999

for tc in range(int(input())):
    before, after = map(int,input().split())

    q = deque()
    visited = [0] * 10001
    q.append([before, ''])

    while q:
        val, char = q.popleft()

        if val == after:
            print(char)
            break

        d = D(val)
        if visited[d] == 0:
            q.append([d, char+'D'])
            visited[d] = 1

        s = S(val)
        if visited[s] == 0:
            q.append([s, char+'S'])
            visited[s] = 1    
        
        l = L(val)
        if visited[l] == 0:
            q.append([l, char+'L'])
            visited[l] = 1  

        r = R(val)
        if visited[r] == 0:
            q.append([r, char+'R'])
            visited[r] = 1  

