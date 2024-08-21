import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dp = [0] * 51

dp[0] = 1
dp[1] = 1

def fibo(n) :
    if dp[n] :
        return dp[n]
    dp[n] = (fibo(n - 2) + fibo(n - 1) + 1) % 1000000007
    return dp[n]

print(fibo(int(input())))