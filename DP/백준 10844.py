import sys
input = sys.stdin.readline

n = int(input())

d = [1] * 10 #마지막 숫자가 이거인 것들의 갯수를 기록
d[0] = 0

for i in range(2, n + 1) :
    nd = [0] * 10
    for j in range(10) :
        if j > 0 :
            nd[j] += d[j - 1]
        if j < 9 :
            nd[j] += d[j + 1]
    d = nd.copy()

    # print(d)
    # print(sum(d))

print(sum(d) % (10**9))