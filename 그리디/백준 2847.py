import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

scores = []

for i in range(n) :
    scores.append(int(input()))

before = scores.pop()

cnt = 0

while scores :
    now = scores.pop()
    minus = 0
    if now >= before :
        minus = now - before + 1
        cnt += minus
    before = now - minus

print(cnt)