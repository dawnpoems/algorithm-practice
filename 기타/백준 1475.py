import sys
import math
from collections import Counter

room_nums = list(map(int, sys.stdin.readline().rstrip()))

counter = Counter(room_nums)

counter[6] = math.ceil((counter[6] + counter[9]) / 2)
counter[9] = counter[6]

print(max(counter.values()))
