import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

start = 1
end = 10000 * N

def can_live(k) :
    times = 0
    money_have = 0
    for i in range(N) :
        if money_have < nums[i] :
            times += 1
            if times > M :
                return False
            money_have = k
        money_have -= nums[i]
        if money_have < 0 :
            return False 
    return True

while start < end :
    mid = (start + end) // 2
    if can_live(mid) :
        end = mid
    else :
        start = mid + 1

print(end)

