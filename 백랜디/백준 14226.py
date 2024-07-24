import sys
input = sys.stdin.readline
from collections import deque

S = int(input())

visited = [[False] * (2 * S + 1) for _ in range(2 * S + 1)]

queue = deque([(1, 0, 0)])

while queue :
    emo, clip, depth = queue.popleft()
    if emo == S :
        print(depth)
        break
    if emo < S :
        if not visited[emo][emo] :
            visited[emo][emo] = True
            queue.append((emo, emo, depth + 1))
        if not visited[emo + clip][clip] :
            visited[emo + clip][clip] = True
            queue.append((emo + clip, clip, depth + 1))
    if emo > 0 and not visited[emo - 1][clip] :
        visited[emo - 1][clip] = True
        queue.append((emo - 1, clip, depth + 1))
