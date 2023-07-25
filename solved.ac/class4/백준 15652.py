import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

n, m = map(int, input().split())

nums = []
for i in range(1, n + 1) :
    nums.append(i)

data = combinations_with_replacement(nums, m)

for d in data :
    print(" ".join(map(str, d)))