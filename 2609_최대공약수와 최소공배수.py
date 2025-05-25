import math

a, b = map(int,input().split())

max_num = math.gcd(a, b)
min_num = max_num * ( a // max_num) * ( b // max_num )

print(max_num)
print(min_num)

