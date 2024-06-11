import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

ans = []
mn = -1
am_idx = -1
bm_idx = -1
while True:
    mn = -1
    i_start = am_idx + 1
    j_start = bm_idx + 1
    for i in range(i_start, N) :
        for j in range(j_start, M) :
            if A[i] == B[j] :
                if mn < A[i] :
                    mn = A[i]
                    am_idx = i
                    bm_idx = j
    if mn == -1 :
        break
    ans.append(mn)
    

print(len(ans))
print(*ans)

# 공통 숫자 중 가장 큰 것 찾기
# 그 뒤 공통 숫자 중 가장 큰 것 찾기. 반복...
# 