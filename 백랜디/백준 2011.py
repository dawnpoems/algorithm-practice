import sys
input = sys.stdin.readline

code = list(map(int, input().strip()))

if code[0] == 0 :
    print(0)
else :
    dp = [0] * (len(code) + 1)

    dp[0] = 1
    dp[1] = 1

    for i in range(2, len(code) + 1) :
        if code[i - 1] > 0 :
            dp[i] += dp[i - 1]
        if code[i - 2] > 0 and code[i - 2] * 10 + code[i - 1] <= 26 :
            dp[i] += dp[i - 2]
    # print(dp)
    print(dp[-1] % 1000000)