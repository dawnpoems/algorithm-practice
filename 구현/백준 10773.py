import sys

input = sys.stdin.readline

n = int(input())

num_list = []

for i in range(n) :
    now = int(input())
    if now == 0 :
        num_list.pop()
    else : 
        num_list.append(now)
    
print(sum(num_list))