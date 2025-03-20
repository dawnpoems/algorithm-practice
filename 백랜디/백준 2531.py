import sys
from collections import deque
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

ate = {}

lines = []

for i in range(N) :
    sushi = int(input())
    lines.append(sushi)
    if sushi not in ate :
        ate[sushi] = 0

ate[c] = 1

mine = deque([])
kind = 1

def add_sushi(now) :
    global kind
    mine.append(now)
    if ate[now] == 0 :
        kind += 1
    ate[now] += 1

def pop_sushi() :
    global kind
    now = mine.popleft()
    ate[now] -= 1
    if ate[now] == 0 :
        kind -= 1

for i in range(k) :
    add_sushi(lines[i])

ans = 0

for i in range(N) :
    now_i = k + i
    if now_i >= N :
        now_i -= N
    pop_sushi()
    add_sushi(lines[now_i])
    # print(mine, kind)
    ans = max(ans, kind)

print(ans)
    