import sys
input = sys.stdin.readline

m = int(input())

S = set()

def addFunc(val):
    S.add(val)

def removeFunc(val):
    if val in S:
        S.remove(val)

def checkFunc(val):
    if val in S:
        print(1, end='\n')
    else:
        print(0, end='\n')

def toggleFunc(val):
    if val in S:
        removeFunc(val)
    else:
        addFunc(val)

def allFunc():
    S.update(range(1,21))

def emptyFunc():
    S.clear()

while m > 0:
    m -= 1

    data = input().split()

    if data[0] == 'add':
        addFunc(int(data[1]))
    elif data[0] == 'remove':
        removeFunc(int(data[1]))
    elif data[0] == 'check':
        checkFunc(int(data[1]))
    elif data[0] == 'toggle':
        toggleFunc(int(data[1]))
    elif data[0] == 'all':
        allFunc()
    else:
        emptyFunc()
    
    # print('S : {}'.format(S))