import sys
input = sys.stdin.readline

one = list(input().strip())
two = list(input().strip())

N = len(one)
M = len(two)

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        if one[i - 1] == two[j - 1] :
            dp[i][j] = dp[i - 1][j - 1] + 1
        else :
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

ans = dp[N][M]
print(ans)

def backtracking(r, c, now) :
    global found
    if found:
        return
    if dp[r][c] == 0 :
        found = True
        return
    if dp[r - 1][c] == now :
        backtracking(r - 1, c, now)
    elif dp[r][c - 1] == now :
        backtracking(r, c - 1, now)
    else :
        ans_lst.append(one[r - 1])
        backtracking(r - 1, c - 1, now - 1)

if ans :
    ans_lst = []
    found = False
    backtracking(N, M, ans)

    ans_lst.reverse()
    print(*ans_lst, sep="")