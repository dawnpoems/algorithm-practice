import sys
input = sys.stdin.readline

N = int(input())
dots = []
for i in range(N) :
    dots.append(list(map(float, input().split())))
dots.append(dots[0])

ans = 0
for i in range(N) :
    ans += dots[i][0] * dots[i + 1][1]
    ans -= dots[i + 1][0] * dots[i][1]

ans /= 2
print(abs(round(ans, 2)))