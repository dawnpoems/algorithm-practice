import sys, math
input = sys.stdin.readline

m = int(input())

f_list = list(map(int, input().split()))

Q = int(input())

mx_log = math.floor(math.log2(500000))
# print(mx_log)

dp = [[0] * (m + 1) for _ in range(mx_log + 1)]

for i in range(1, m + 1) :
    dp[0][i] = f_list[i - 1]

for k in range(1, mx_log + 1) :
    for i in range(1, m + 1) :
        dp[k][i] = dp[k - 1][dp[k - 1][i]]

# print(dp)

for q in range(Q) :
    n, x = map(int, input().split())
    pos = x
    i = mx_log
    # print(n, x)
    while i >= 0 :
        if n & (1 << i) :
            pos = dp[i][pos]
            # print(n & (i << 1))
        i -= 1
    print(pos)
    # print("--------------")
