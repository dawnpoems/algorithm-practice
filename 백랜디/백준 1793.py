import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

dp = [0] * 251

dp[0] = 1
dp[1] = 1

def get_nums(n) :
    if dp[n] != 0 :
        return dp[n]
    else :
        dp[n] = get_nums(n - 2) * 2 + get_nums(n - 1)
        return dp[n]

while True :
    try :
        N = int(input())
        print(get_nums(N))
    except :
        break
