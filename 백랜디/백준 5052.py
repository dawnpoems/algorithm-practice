import sys
input = sys.stdin.readline

T = int(input())

def is_prefix(i, N) :
    for j in range(i + 1, N) :
        prefix = True
        for k in range(len(nums[i])) :
            if nums[i][k] != nums[j][k] :
                prefix = False
                break
        if prefix :
            return True 
    return False

for t in range(T) :
    N = int(input())
    nums = []
    for i in range(N) :
        nums.append(input().strip())
    nums.sort(key=lambda x : len(x))
    flag = True
    for i in range(N) :
        if is_prefix(i, N) :
            flag = False
            break
    if flag :
        print("YES")
    else :
        print("NO")
                

    



    