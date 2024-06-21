import sys
input = sys.stdin.readline

N, K = map(int, input().split())

mod = 1000000007

def dac(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c


def fac(n) :
    global mod
    ans = 1
    for i in range(2, n + 1) :
        ans = (ans * i) % mod
    return ans
    
ans = (fac(N)) * dac(fac(K), mod - 2, mod) * dac(fac(N - K), mod - 2, mod)
print(ans % mod)

#분할 정복을 사용한 거듭제곱과 페르마의 소정리를 이용해 곱셈의 역원을 구하는 문제