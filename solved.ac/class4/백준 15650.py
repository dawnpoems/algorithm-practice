import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

nums = []
for i in range(1, n + 1) :
    nums.append(i)

data = combinations(nums, m)

for d in data :
    print(" ".join(map(str, d)))