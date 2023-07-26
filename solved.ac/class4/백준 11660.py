import sys
input = sys.stdin.readline

n, m = map(int, input().split())

board = []
totals = []
for i in range(n) :
    row = list(map(int, input().strip().split()))
    board.append(row)
    total_row = []
    cnt = 0
    for j in range(n) :
        up = 0
        if i > 0 :
            up = totals[i - 1][j]
        cnt += row[j]
        total_row.append(up + cnt)
    totals.append(total_row)

# print()
# print("-----------")
# for row in totals :
#     print(" ".join(map(str, row)))

# print("-------------")

for i in range(m) :
    r1, c1, r2, c2 = map(int, input().split())
    r_minus = 0
    c_minus = 0
    rc_plus = 0
    flag = [False, False]
    if r1 - 2 >= 0 : 
        flag[0] = True
        r_minus = totals[r1-2][c2-1]
    if c1 - 2 >= 0 :
        flag[1] = True
        c_minus = totals[r2-1][c1-2]
    if False not in flag :
        rc_plus = totals[r1-2][c1-2]
    result = totals[r2-1][c2-1] - r_minus - c_minus + rc_plus
    # print("result = ", end="")
    print(result)

