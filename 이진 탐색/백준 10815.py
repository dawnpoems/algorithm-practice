import sys
input = sys.stdin.readline

n = int(input())

cards = list(map(int, input().strip().split()))

m = int(input())

nums = list(map(int, input().strip().split()))

cards.sort()

for num in nums :
    start = 0
    end = len(cards) - 1
    found = False

    while start <= end :
        mid = (start + end) // 2
        now = cards[mid]
        if now == num :
            found = True
            break
        elif now < num :
            start = mid + 1
        else :
            end = mid - 1
    if found :
        print(1, end=" ")
    else :
        print(0, end=" ")