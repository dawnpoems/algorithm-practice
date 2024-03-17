import sys

n = int(sys.stdin.readline())
conditions = list(map(int, sys.stdin.readline().split()))

for c in conditions:
    if c > 0:
