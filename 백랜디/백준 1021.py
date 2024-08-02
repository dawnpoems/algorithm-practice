import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

queue = deque()

for i in range(N) :
    queue.append(i + 1)

def left_rotate() :
    now = queue.popleft()
    queue.append(now)

def right_rotate() :
    now = queue.pop()
    queue.appendleft(now)

nums = list(map(int, input().split()))

ans = 0
for idx in nums :
    for i in range(len(queue)) :
        if queue[i] == idx :
            break
    # print(i)
    if i < len(queue) - i :
        j = 0
        while j < i :
            left_rotate()
            ans += 1
            j += 1
    else :
        j = 0
        while j < len(queue) - i :
            right_rotate()
            j += 1
            ans += 1
    queue.popleft()
    # print(queue)

print(ans)
    
            
