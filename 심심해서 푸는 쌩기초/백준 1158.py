import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([])

for i in range(1, N + 1) :
    queue.append(i)
print("<", end="")

cnt = 0
while len(queue) > 1 :
    cnt += 1
    now = queue.popleft()
    if cnt == K :
        print(now, end=", ")
        cnt = 0
    else :
        queue.append(now)

print(queue.popleft(), ">", sep="")