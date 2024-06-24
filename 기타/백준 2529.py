import sys
input = sys.stdin.readline

N = int(input())

inq = input().split()

ans_big = [[9]]
ans_small = [[0]]

idx_big = 0
idx_small = 0

for i in range(N) :
    if inq[i] == '>' :
        ans_big.append([9 - i - 1])
        idx_big += 1
        ans_small[idx_small].append(i + 1)
    else :
        ans_big[idx_big].append(9 - i - 1)
        ans_small.append([i + 1])
        idx_small += 1

for ab in ans_big :
    print(*reversed(ab), sep="", end="")

print()
for a_s in ans_small :
    print(*reversed(a_s), sep="", end="")