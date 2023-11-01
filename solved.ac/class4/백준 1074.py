import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())
rc = [r, c]
cnt = 0

def zet(depth, row, col) :
    global cnt
    # print(row, end=" ")
    # print(col, end=" ")
    # print(cnt)
    if depth < 0 :
        return
    if rc[0] == row and rc[1] == col :
        print(cnt)
        return 
    if rc[0] < row + 2**(depth - 1) :
        if rc[1] < col + 2**(depth - 1) :
            zet(depth - 1, row, col)
        else :
            cnt += 2**((depth - 1) * 2)
            zet(depth - 1, row, col + 2**(depth - 1))
    else :
        if rc[1] < col + 2**(depth - 1) :
            cnt += (2**((depth - 1) * 2)) * 2
            zet(depth - 1, row + 2**(depth - 1), col)
        else :
            cnt += (2**((depth - 1) * 2)) * 3
            zet(depth - 1, row + 2**(depth - 1), col + 2**(depth - 1))

zet(n, 0, 0)