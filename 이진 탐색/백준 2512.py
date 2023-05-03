import sys

n = int(sys.stdin.readline())
requests = list(map(int, sys.stdin.readline().split()))
money = int(sys.stdin.readline())


# 매번 하는 그 이진탐색 알고리즘
start = 0
end = max(requests)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0
    # total 값 계산
    for i in requests:
        if mid <= i:
            total += mid
        else:
            total += i
    if total == money:
        result = mid
        break
    elif total < money:
        result = mid  # 최댓값을 찾고 있으므로 이 값도 result에 넣어주기
        start = mid + 1
    else:
        end = mid - 1

print(result)
