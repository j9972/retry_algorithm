import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
white, blue = 0,0

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def same(x,y,size):
    color = arr[x][y]

    for i in range(x,x+size):
        for j in range(y,y+size):
            if color != arr[i][j]:
                return False
    return True

def sol(x,y,size):
    global white, blue

    if size == 1:
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1
        return
    
    if same(x,y,size):
        if arr[x][y] == 0:
            white += 1
        else:
            blue += 1   
        return 
    
    half = size // 2

    sol(x,y,half)
    sol(x+half,y,half)
    sol(x,y+half,half)
    sol(x+half,y+half,half)

sol(0,0,n)
print(white)
print(blue)
    
