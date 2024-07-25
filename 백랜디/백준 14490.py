import sys
input = sys.stdin.readline

N, M = map(int, input().split(":"))

n = N
m = M

i = min(n, m)
while i > 1 :
    if n % i == 0 and m % i == 0 :
        n //= i
        m //= i
        i = min(n, m)
    i -= 1
    
print(n, ":", m, sep="")