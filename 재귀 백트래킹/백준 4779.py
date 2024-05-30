import sys
input = sys.stdin.readline

def change_space(start, len) :
    if len < 1 :
        return
    one_third = start + len
    two_third = start + len * 2
    for i in range(one_third, two_third) :
        cantor_lst[i] = False
    change_space(start, len // 3)
    change_space(two_third, len // 3)

while True :
    str = input()
    if not str :
        break
    N = 3 ** int(str)
    cantor_lst = [True] * N
    change_space(0, N // 3)
    for i in range(N) :
        if cantor_lst[i] :
            print("-", end="")
        else :
            print(" ", end="")
    print()
