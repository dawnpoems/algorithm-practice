import sys
input = sys.stdin.readline

nums = [i for i in range(10001)]

def get_loof_num(n) :
    now = n
    ret = n
    while now > 0 :
        ret += now % 10
        now //= 10
    return ret

for i in range(1, 10001) :
    if nums[i] == - 1:
        continue
    print(i)
    now = i
    while True :
        now = get_loof_num(now)
        if now > 10000 :
            break
        nums[now] = -1