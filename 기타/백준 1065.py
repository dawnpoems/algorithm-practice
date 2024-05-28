import sys
input = sys.stdin.readline

N = int(input())

def is_hansu(n) :
    if n < 100 :
        return True
    before_digit = n % 10
    after_digit = (n // 10) % 10
    arith = before_digit - after_digit
    now = n // 100
    while now > 0 :
        before_digit = after_digit
        after_digit = now % 10
        if arith != before_digit - after_digit :
            return False
        now = now // 10
    return True

ans = 0

for i in range(1, N + 1) :
    if is_hansu(i) :
        ans += 1

print(ans)