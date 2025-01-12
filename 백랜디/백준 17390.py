import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

accum = [0]

for i in range(N) :
    accum.append(accum[i] + nums[i])

for i in range(Q) :
    L, R = map(int, input().split())

    print(accum[R] - accum[L - 1])

