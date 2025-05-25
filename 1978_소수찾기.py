n =  int(input())

arr = list(map(int,input().split()))
tot = 0

def prime(n):

    if n <= 1:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
            
    return True

for i in arr:
    if(prime(i)):
        tot += 1

print(tot)