import sys
input = sys.stdin.readline

dest = int(input().strip())

M = int(input())
if M :
    brock = list(map(int, input().split()))
else :
    brock = []

def check_fine(num) :
    if num == 0 :
        if num in brock :
            return 0
    while num > 0 :
        digit = num % 10
        if digit in brock :
            return 0
        num = num // 10
    return 1

big = dest
small = dest
start = abs(dest - 100)

big_cnt = 0
small_cnt = 0

big_end = 0
small_end = 0
while True :
    if big_end and small_end :
        break
    if big_end and big_cnt < small_cnt :
        break
    if small_end and big_cnt > small_cnt :
        break
    if big_end == 0:
        if check_fine(big) :
            big_end = 1
            big_cnt += len(str(big))
        else :
            big += 1
            big_cnt += 1
    if small_end == 0 :
        if small < 0 :
            small_end = 1
            small_cnt = 500000
        elif check_fine(small) :
            small_end = 1
            small_cnt += len(str(small))
        else :
            small -= 1
            small_cnt += 1

print(min(big_cnt, small_cnt, start))