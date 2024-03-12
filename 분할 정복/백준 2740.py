import sys
input = sys.stdin.readline

AN, AM = map(int, input().split())

matrix_a = []
for i in range(AN) :
    matrix_a.append(list(map(int, input().split())))

BN, BM = map(int, input().split())

matrix_b = []
for i in range(BN) :
    matrix_b.append(list(map(int, input().split())))

ans = []

for i in range(AN) :
    line = []
    for j in range(BM) :
        now = 0
        for k in range(AM) :
            now += matrix_a[i][k] * matrix_b[k][j]
        line.append(now)
    ans.append(line)

for i in range(AN) :
    print(" ".join(map(str, ans[i])))