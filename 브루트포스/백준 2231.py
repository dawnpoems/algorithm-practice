import sys
input = sys.stdin.readline

n = int(input())

answer = 0
for i in range(1, n) :
    apart_num = i
    for j in list(str(i)) :
        apart_num += int(j)
    
    if apart_num == n :
        answer = i
        break

print(answer)