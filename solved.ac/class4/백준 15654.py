import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().strip().split()))

nums.sort()

data = permutations(nums, m)

for d in data :
    print(" ".join(map(str, d)))