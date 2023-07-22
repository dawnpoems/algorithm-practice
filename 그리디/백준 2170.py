import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lines = []

for i in range(n) :
    x, y = map(int, input().strip().split())
    lines.append([x, y])

answers = deque([lines.pop()])

for line in lines :
    start = line[0]
    end = line[1]
    # print(answers)
    # print(line)
    for i in range(len(answers)) :
        ans = answers.popleft()
        if end <= ans[0] or start >= ans[1] :
            answers.append([ans[0], ans[1]])
        else :
            if start > ans[0] :
                start = ans[0]
            if end < ans[1] :
                end = ans[1]
    # print(start, end)
    answers.append([start, end])

cnt = 0
while answers :
    l = answers.pop()
    cnt += l[1]- l[0]

print(cnt)
