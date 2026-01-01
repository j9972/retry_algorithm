import sys
input = sys.stdin.readline

# input = sys.stdin.read

n = int(input().strip())

if n == 0:
    print(0)
else:    
    data = sorted(int(input().strip()) for _ in range(n))

    half_ = int(n*0.15+0.5)
    print(int(sum(data[half_:n-half_])/(n-2*half_) + 0.5))


