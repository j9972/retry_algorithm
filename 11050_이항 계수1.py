n, k = map(int,input().split())

def factorial(n):
    if n <= 1 :
        return 1
    else:
        return factorial(n-1) * n

print(factorial(n)//(factorial(k)*factorial(n-k)))

