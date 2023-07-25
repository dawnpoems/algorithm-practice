import sys
input = sys.stdin.readline

n = int(input())

totals = [[0, 0, 0]]
for i in range(n) :
    r, g, b = map(int, input().strip().split())
    red = min(totals[i][1], totals[i][2]) + r
    green = min(totals[i][0], totals[i][2]) + g
    blue = min(totals[i][0], totals[i][1]) + b
    totals.append([red, green, blue])

# print(totals)
print(min(totals[-1]))
    