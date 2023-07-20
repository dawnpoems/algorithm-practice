import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

cnts = [-1] * (n + 1)

queue = deque([n])
cnts[n] = 0

while queue :
    v = queue.popleft()
    if v == 1 :
        break

    if v % 3 == 0 and cnts[v//3] == -1 :
        cnts[v//3] = cnts[v] + 1
        queue.append(v // 3)
    if v % 2 == 0 and cnts[v//2] == -1 :
        cnts[v//2] = cnts[v] + 1
        queue.append(v // 2)
    if v -1 > 0 and cnts[v-1] == -1 :
        cnts[v-1] = cnts[v] + 1
        queue.append(v - 1)

# print(cnts)

print(cnts[1])