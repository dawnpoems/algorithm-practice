import sys
input = sys.stdin.readline

n = int(input())

five = n//5

count = -1
for i in range(five, -1, -1):
    three = n - 5*i
    if three % 3 == 0:
        count = i + (three // 3)
        break

print(count)
