import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

queue = deque([(a, 1)])

found = False

while queue :
    v = queue.popleft()
    if v[0] == b :
        print(v[1])
        found = True
        break
    double = v[0] * 2
    if double <= b :
        queue.append((double, v[1] + 1))
    one = int(str(v[0]) + "1")
    if one <= b :
        queue.append((one, v[1] + 1))

if not found :
    print(-1)