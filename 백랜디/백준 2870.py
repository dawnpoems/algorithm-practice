import sys
input = sys.stdin.readline

N = int(input())

nums = []

def is_num_str(s) :
    if ord('0') <= ord(s) <= ord('9') :
        return True
    else :
        return False

for j in range(N) :
    line = list(input().strip())
    i = 0
    while i < len(line) :
        while i < len(line) and is_num_str(line[i]) == False:
            i += 1
        if i >= len(line) :
            break
        num = 0
        while i < len(line) and is_num_str(line[i]) :
            num = num * 10 + int(line[i])
            i += 1
        nums.append(num)

for n in sorted(nums) :
    print(n)
        
        