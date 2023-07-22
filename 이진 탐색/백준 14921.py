import sys
input = sys.stdin.readline

n = int(input())

solutions = list(map(int, input().strip().split()))

solu = solutions[0] + solutions[1]

for i in range(n - 1) :
    s = solutions[i]
    start = i + 1
    end = n - 1
    while start <= end :
        mid = (start + end) // 2
        now = s + solutions[mid]
        if abs(solu) >= abs(now) :
            solu = now
        if now == 0 :
            break
        elif now < 0 :
            start = mid + 1
        else :
            end = mid - 1

print(solu)
            
            

