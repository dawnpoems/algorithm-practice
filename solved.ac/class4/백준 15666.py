import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement

n, m = map(int, input().split())

nums = list(map(int, input().strip().split()))

nums.sort()
data = combinations_with_replacement(nums, m)

data = list(set(data))
data.sort()

for d in data :
    print(" ".join(map(str, d)))