import sys
input = sys.stdin.readline

m, n = map(int,input().split())

arr = [
    list(input().strip())
    for _ in range(m)
]

new_arr = [
    [[] for _ in range(8)] 
    for _ in range(8)
]

max_cnt = 10e9

startWithWhite = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W']
]

startWithBlack = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]

def counting():
    startWithBlackCnt, startWithWhiteCnt = 0, 0
    # print("counting > ", new_arr)

    for x in range(8):
        for y in range(8):
            if new_arr[x][y] != startWithBlack[x][y]:
                startWithBlackCnt += 1

    for x in range(8):
        for y in range(8):
            if new_arr[x][y] != startWithWhite[x][y]:
                startWithWhiteCnt += 1

    # print("startWithBlackCnt : {} , startWithWhiteCnt : {} ".format(startWithBlackCnt, startWithWhiteCnt))
    
    return min(startWithBlackCnt, startWithWhiteCnt)


for x in range(m-7):
    for y in range(n-7):

        for i in range(8):
            for j in range(8):
                new_arr[i][j] = arr[x+i][y+j]
        
        # print("for문속 > ", new_arr)
        # print(x,y)
        max_cnt = min(max_cnt, counting())
        # print(max_cnt)

print(max_cnt)

