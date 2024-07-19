import sys
input = sys.stdin.readline

N = int(input())

red = 0
blue = 0

pros = list(input().strip())

prev = "X"

for p in pros :
    if p == "R" and p != prev :
        red += 1
    if p == "B" and p != prev :
        blue += 1
    prev = p

# print(red, blue)
print(min(red, blue) + 1)