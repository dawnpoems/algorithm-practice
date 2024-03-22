import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

start = 0
end = 0

found = 0
best_len = 1e9

total = 0
while True :
    # print(start, end, total)
    if total < S :
        if end >= N :
            break
        total += nums[end]
        end += 1
    else :
        if end - start < best_len :
            best_len = end - start
        found = 1
        total -= nums[start]
        start += 1

if found :
    print(best_len)
else :
    print(0)