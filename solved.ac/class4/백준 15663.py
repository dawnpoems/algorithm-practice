import sys
input = sys.stdin.readline
from itertools import permutations

n, m = map(int, input().split())

nums = list(map(int, input().strip().split()))

data = permutations(nums, m)

data = list(set(data))
data.sort()

for d in data :
    print(" ".join(map(str, d)))