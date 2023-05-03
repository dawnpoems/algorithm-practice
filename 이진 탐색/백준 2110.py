import sys

n, c = map(int, sys.stdin.readline().split())

homes = []

for i in range(n):
    homes.append(int(sys.stdin.readline()))

homes.sort()

# 거리순 / 조합 /
