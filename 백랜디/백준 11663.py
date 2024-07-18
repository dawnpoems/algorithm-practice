import sys, bisect
input = sys.stdin.readline

N, M = map(int, input().split())

dots = list(map(int, input().split()))
dots.sort()

for i in range(M) :
    a, b = map(int, input().split())
    idx_a = bisect.bisect_left(dots, a)
    idx_b = bisect.bisect_right(dots, b)
    print(idx_b - idx_a)
    