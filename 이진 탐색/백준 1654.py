import sys

k, n = map(int, sys.stdin.readline().split())

lans = []

for i in range(k):
    lans.append(int(sys.stdin.readline()))

start = 1
end = max(lans)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    for lan in lans:
        total += (lan // mid)
    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
