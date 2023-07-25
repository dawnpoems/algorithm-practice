import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [0] * (k + 1)

for i in range(n) :
    w, v = map(int, input().strip().split())
    for j in range(k, -1, -1) :
        if j >= w :
            d[j] = max(d[j], d[j - w] + v)
    # print("------")
    # print(w, v)
    # print(d)

print(d[k])