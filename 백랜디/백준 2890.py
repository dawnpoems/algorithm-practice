import sys
input = sys.stdin.readline

R, C = map(int, input().split())

pos = [0] * 10

for i in range(R) :
    line = list(input().strip())
    for j in range(1, C - 1) :
        if line[j].isdigit() :
            pos[int(line[j])] = j
            break

ranks = [0] * 10

rank_now = 1
for i in range(C - 4, 0, -1) :
    has_rank = False
    for j in range(1, 10) :
        if pos[j] == i :
            ranks[j] = rank_now
            has_rank = True
    if has_rank :
        rank_now += 1

for i in range(1, 10) :
    print(ranks[i])