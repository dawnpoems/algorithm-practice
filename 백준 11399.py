import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

times.sort()

min_time = 0

for i in range(len(times)):
    min_time += times[i] * (len(times) - i)

print(min_time)
