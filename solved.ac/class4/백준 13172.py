import sys, math
input = sys.stdin.readline

M = int(input())

exps = []

mod = 1000000007

def get_inverse(a, p) :
    
    if p == 1 :
        return 0
    return pow(a, p - 2, p)

for i in range(M) :
    b, a = list(map(int, input().split()))
    gcd = math.gcd(a, b)
    a //= gcd
    b //= gcd
    exp = (a * get_inverse(b, mod)) % mod
    exps.append(exp)

print(sum(exps) % mod)