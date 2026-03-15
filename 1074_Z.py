n,x,y = map(int,input().split())

ans = 0

while n > 0:

    half = 2 ** (n - 1)
    area = half ** 2

    # 1사분면
    if x < half and y < half:
        ans += 0 * area

    # 2사분면
    elif x < half and y >= half:
        ans += 1 * area
        y -= half

    # 3사분면
    elif x >= half and y < half:
        ans += 2 * area
        x -= half

    # 4사분면
    else:
        ans += 3 * area
        x -= half
        y -= half
    n -= 1

print(ans)