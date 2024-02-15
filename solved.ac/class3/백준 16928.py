import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ladder = [0] * 101
snake = [0] * 101

for i in range(N) :
    start, end = map(int, input().split())
    ladder[start] = end

for i in range(M) :
    start, end = map(int, input().split())
    snake[start] = end

def bfs() :
    queue = deque([])
    queue.append((1, 0))
    while (queue) :
        now = queue.popleft()
        i = 6
        flag = 0
        while (i > 0) :
            nxt = i + now[0]
            if (nxt >= 100) :
                return (now[1] + 1)
            if (ladder[nxt] != 0) :
                queue.append((ladder[nxt], now[1] + 1))
            elif (snake[nxt] != 0) :
                queue.append((snake[nxt], now[1] + 1))
            elif (flag == 0) :
                flag = 1
                queue.append((nxt, now[1] + 1))
            i -= 1

print(bfs())