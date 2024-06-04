import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

dp = [[0] * 2 for _ in range(N + 1)]

dp[1][0] = 1
dp[1][1] = 1

def find_ans(n, c) :
    if dp[n][c] :
        return dp[n][c]
    if c == 0 :
        dp[n][c] = (find_ans(n - 1, 0) + find_ans(n - 1, 1) * 2) % 9901
    if c == 1 :
        dp[n][c] = (find_ans(n - 1, 0) + find_ans(n - 1, 1)) % 9901
    return dp[n][c]

print((find_ans(N, 0) + find_ans(N, 1) * 2) % 9901)