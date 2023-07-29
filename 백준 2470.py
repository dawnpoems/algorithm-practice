import sys
input = sys.stdin.readline

n = int(input())

solutions = list(map(int, input().strip().split()))

start = 0
end = n - 1

solutions.sort()

cnt = solutions[start] + solutions[end]
answer = (solutions[start], solutions[end])

while start < end :
    now = solutions[start] + solutions[end]
    if abs(now) < abs(cnt) :
        cnt = now
        answer = (solutions[start], solutions[end])
    if now == 0 :
        break
    elif now < 0 :
        start += 1
    else :
        end -= 1

print(answer[0], answer[1])