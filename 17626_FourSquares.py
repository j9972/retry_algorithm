import sys
input = sys.stdin.readline

n = int(input())

for i in range(1,int(n**0.5)+1):
    if i ** 2 == n:
        print(1)
        sys.exit()

for i in range(1,int(n**0.5)+1):
    remain = n - i ** 2
    j = int(remain ** 0.5)

    if j ** 2 == remain:
        print(2)
        sys.exit()

for i in range(1, int(n**0.5) + 1):
    for j in range(i, int((n - i**2) ** 0.5) + 1):
        remain = n - i**2 - j**2

        k = int(remain ** 0.5)

        if k ** 2 == remain:
            print(3)
            sys.exit()
print(4)

