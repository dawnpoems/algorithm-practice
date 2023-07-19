import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

m = int(input())
targets = list(map(int, input().split()))

cards.sort()

def find_start(cards, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # print(mid)
        num = cards[mid]
        if num == target:
            if mid == 0 or cards[mid -1] != target:
                return mid
            else :
                end = mid - 1
        elif num > target :
            end = mid - 1
        else :
            start = mid + 1
    return None

def find_end(cards, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # print(mid)
        num = cards[mid]
        if num == target:
            if mid == n - 1 or cards[mid + 1] != target:
                return mid
            else :
                start = mid + 1
        elif num > target :
            end = mid - 1
        else :
            start = mid + 1
    return None


# print(cards)

for target in targets :
    s = find_start(cards, target, 0, n-1)
    # print("-------")
    answer = 0
    if s != None :
        e = find_end(cards, target, s, n-1)
        answer = e - s + 1
    print(answer, end=" ")





