import sys
from itertools import *

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))

sum_list = []

comb_list = combinations(cards, 3)
for comb in comb_list :
    sum_comb = sum(comb)
    if sum_comb <= m :
        sum_list.append(sum_comb)

print(max(sum_list))


