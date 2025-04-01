import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = []

for i in range(N) :
    nums.append(int(input()))

nums.sort()

for i in range(M) :
    target = int(input())
    start = 0
    end = N - 1
    ans = -1
    while start <= end :
        mid = (start + end) // 2
        if target < nums[mid] :
            end = mid - 1
        elif target == nums[mid] :
            ans = mid
            end = mid - 1
        else :
            start = mid + 1
    print(ans)


