import sys

n = int(sys.stdin.readline())

jungsus = list(map(int, sys.stdin.readline().split()))

target = int(sys.stdin.readline())

answer = 0
for i in jungsus:
    if target == i:
        answer += 1

print(answer)
