import sys

n = int(sys.stdin.readline())

answer = 0
count = 0
natual = 0
while True:
    natual += 1
    count += natual
    answer += 1
    if count > n:
        break

print(answer - 1)
