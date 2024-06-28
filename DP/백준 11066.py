import sys
input = sys.stdin.readline

T = int(input())

INF = int(1e9)

def memo(start, end) :
    if start == end :
        return 0
    if dp[start][end] != INF:
        return dp[start][end]
    
    total = subTotal[end + 1] - subTotal[start]
    for i in range(start, end) :
        dp[start][end] = min(dp[start][end], memo(start, i) + memo(i + 1, end) + total)
    # print(start, end, total, dp[start][end])
    return dp[start][end]
    

for t in range(T) :
    N = int(input())
    files = list(map(int, input().split()))

    dp = [[INF] * (N) for _ in range(N)] #시작지점이 r, 끝지점이 c. 이때의 값
    subTotal = [0] * (N + 1)
    
    for i in range(N) :
        dp[i][i] = files[i]
    
    for i in range(1, N + 1) :
        subTotal[i] = subTotal[i - 1] + files[i - 1] 
    # print(subTotal)
    
    ans = memo(0, N - 1)
    # print(dp)
    print(ans)