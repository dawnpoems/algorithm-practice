import sys, math, copy
input = sys.stdin.readline

N, B = map(int, input().split())

matrix = []

for i in range(N) :
    matrix.append(list(map(lambda x : x % 1000, map(int, input().split()))))

def matrix_mul(one, two) :
    global N
    result = [[0] * N for _ in range(N)]
    for r in range(N) :
        for c in range(N) :
            for k in range(N) :
                result[r][c] += one[r][k] * two[k][c]
            result[r][c] = result[r][c] % 1000
    return result

dp = []

dp.append(matrix)
for i in range(int(math.log2(B) + 1)) :
    dp.append(matrix_mul(dp[-1], dp[-1]))

# for d in dp :
#     print(d)

def get_ans(B) :
    lower = int(math.log2(B))
    nxt = B - (2 ** lower)
    if nxt :
        return matrix_mul(dp[lower], get_ans(nxt))
    else :
        return dp[lower]

for ans in get_ans(B) :
    print(*ans)