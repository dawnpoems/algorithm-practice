import sys
input = sys.stdin.readline

while True :
    line = list(map(int, input().split()))
    length = line[0]
    if length == 0 :
        break
    
    zero = 0
    nums = []
    for i in range(1, length + 1) :
        if line[i] == 0 :
            zero += 1
        else :
            nums.append(line[i])
    nums.sort(reverse=True)
    # print(nums)
    ans1 = nums.pop()
    ans2 = nums.pop()
    
    while zero or nums :
        if zero :
            ans1 *= 10
            zero -= 1
        else :
            ans1 = ans1 * 10 + nums.pop()
        if zero == 0 and len(nums) == 0 :
            break
        if zero :
            ans2 *= 10
            zero -= 1
        else :
            ans2 = ans2 * 10 + nums.pop()
    # print(ans1, ans2)
    print(ans1 + ans2)
    