import sys
input = sys.stdin.readline

nameToNumber = {}
numberToName = []

n,m = map(int,input().split())

for i in range(1,n+1):
    pocketmon = input().strip()

    nameToNumber[pocketmon] = i
    numberToName.append(pocketmon)

for i in range(m):
    val = input().strip()

    if val.isdigit():
        print(numberToName[int(val)-1])
    else:
        print(nameToNumber[val])
    