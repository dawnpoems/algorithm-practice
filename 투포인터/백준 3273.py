import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
X = int(input())

nums.sort()

start = 0
end = N - 1
cnt = 0

while start < end :
    now = nums[start] + nums[end]
    if now == X :
        cnt += 1
    if now < X :
        start += 1
    else :
        end -= 1

print(cnt)