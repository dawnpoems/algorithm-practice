import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

lst = []
while True :
    now = input()
    if not now :
        break
    lst.append(int(now))

def tour(start, end) :
    mid = start
    left = start + 1
    right = left
    while right <= end and lst[right] < lst[mid] :
        right += 1
    if left <= right - 1 :
        tour(left, right - 1)
    if right <= end :
        tour(right, end)
    print(lst[mid])

tour(0, len(lst) - 1)