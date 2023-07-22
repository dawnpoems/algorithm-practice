import sys
input = sys.stdin.readline

numbers = list(input())

start = None

cnt = [0, 0]
start = numbers.pop()

while numbers :
    now = numbers.pop()
    if now != start :
        if now == "1" :
            cnt[1] += 1
        else :
            cnt[0] += 1
        start = now

print(min(cnt))