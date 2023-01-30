from heapq import heappop, heappush
import sys

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap))

    else:
        heappush(heap, num)
