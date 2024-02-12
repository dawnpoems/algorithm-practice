import sys
input = sys.stdin.readline

N, K = map(int, input().split())

sum_lst = [0]
tmp = list(map(int, input().split()))

now = 0
for t in tmp :
    now += t
    sum_lst.append(now)

ans = (-1) * (10 ** 8)
# print(sum_lst)

for s in range(N - K + 1) :
    ans = max(ans, sum_lst[s + K] - sum_lst[s])
    # print(sum_lst[s + K] - sum_lst[s])

print(ans)