import sys
input = sys.stdin.readline

N, X = map(int, input().split())

visit_nums = list(map(int, input().split()))

cum_sum = [0]

s = 0
for i in range(N) :
    s += visit_nums[i]
    cum_sum.append(s)

start = 0
end = X

mx = 0
mx_cnt = 0

while end < len(cum_sum) :
    now = cum_sum[end] - cum_sum[start]
    if mx < now :
        mx = now
        mx_cnt = 1
    elif mx == now :
        mx_cnt += 1
    start += 1
    end += 1

if not mx :
    print("SAD")
else :
    print(mx)
    print(mx_cnt) 