import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

route = list(map(int, input().strip().split()))

def get_nxt_power(start, end) :
    if start == 0 :
        return 2
    if start == end :
        return 1
    if abs(end - start) == 2 :
        return 4
    return 3

dp = [[[-1] * len(route) for _ in range(5)] for _ in range(5)]

def solve(l, r, i) :
    if route[i] == 0 :
        return 0
    if dp[l][r][i] != -1 :
        return dp[l][r][i]
    left = solve(route[i], r, i + 1) + get_nxt_power(l, route[i])
    right = solve(l, route[i], i + 1) + get_nxt_power(r, route[i])
    dp[l][r][i] = min(left, right)
    return dp[l][r][i]    

# def backtracking(left, right, power, idx) :
#     global ans
#     if route[idx] == 0 :
#         ans = min(ans, power)
#         return
#     i = route[idx]
#     if right != i :
#         backtracking(i, right, power + get_nxt_power(left, i), idx + 1)
#     if left != i :
#         backtracking(left, i, power + get_nxt_power(right, i), idx + 1)

print(solve(0, 0, 0))
for i in range(len(route)) :
    print(*dp[i])
# backtracking(0, 0, 0, 0)
# print(ans)
