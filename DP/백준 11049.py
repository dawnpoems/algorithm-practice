import sys
input = sys.stdin.readline

N = int(input())

matrix = []

for i in range(N) :
    matrix.append(list(map(int, input().split())))

INF = int(1e9)
dp = [[INF] * N for _ in range(N)] #dp[시작행렬][끝행렬] = 연산횟수 최솟값

for i in range(N) :
    dp[i][i] = 0

for i in range(1, N) : #간격이 작은 값부터 계산
    start = 0
    while start + i < N : #앞에서부터 순회하며 계산
        for mid in range(start, start + i) :
            dp[start][start + i] = min(dp[start][start + i],
                                       dp[start][mid] + dp[mid + 1][start + i] + matrix[start][0] * matrix[mid][1] * matrix[start + i][1])
        start += 1

# print(dp)
print(dp[0][N - 1])
