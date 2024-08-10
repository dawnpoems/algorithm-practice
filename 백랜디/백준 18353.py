import sys, bisect
input = sys.stdin.readline

N = int(input())

powers = list(map(int, input().split()))

line = []

for i in range(N) :
    if not line or line[-1] < -powers[i] :
        line.append(-powers[i])
    else :
        idx = bisect.bisect_left(line, -powers[i])
        line[idx] = -powers[i]

print(N - len(line))