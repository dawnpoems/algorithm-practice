import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
dp = defaultdict(int)

dp[0] = 0
dp[1] = 1
dp[2] = 1

def fibo(n) :
    if not dp[n] :
        if n & 1 :
            fn = fibo(n // 2)
            fn_plus = fibo(n // 2 + 1)
            dp[n] = (fn ** 2 + fn_plus ** 2) % 1000000007
        else :
            fn = fibo(n // 2)
            fn_minus = fibo(n // 2 - 1)
            dp[n] = (fn * (fn + 2 * fn_minus)) % 1000000007
    return dp[n]

print(fibo(N))