import sys

n = int(sys.stdin.readline())
mountains = list(map(int, sys.stdin.readline().split()))

count = 0
high_san = 0

counts = []

for san in mountains:
    if san > high_san:
        counts.append(count)
        high_san = san
        count = 0
    else:
        count += 1

counts.append(count)

print(max(counts))
