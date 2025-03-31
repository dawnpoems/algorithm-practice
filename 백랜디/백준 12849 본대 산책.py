import sys
input = sys.stdin.readline

D = int(input())

'''
0. 정보과학관
1. 전산관
2. 미래관
3. 한경직기념관
4. 형남공학관
5. 신양관
6. 진리관
7. 학생회관
'''

graph = [[1, 2], [0, 2, 5], [0, 1, 3, 5],
          [2, 4, 5, 6], [3, 7], [1, 2, 3, 6],
          [3, 5, 7], [6, 4]]

dp = [[0] * 8 for _ in range(D + 1)]
dp[0][0] = 1

for i in range(1, D + 1) :
    for j in range(8) :
        for g in graph[j] :
            dp[i][j] = (dp[i][j] + dp[i - 1][g]) % 1000000007

print(dp[D][0])