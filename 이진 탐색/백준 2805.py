import sys

n, m = map(int, sys.stdin.readline().split())
namus = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(namus)

result = 0
while start <= end:
    mid = (end + start) // 2
    total = 0
    for i in namus:
        if i > mid:
            total += (i - mid)
    if total == m:
        result = mid
        break
    elif total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
