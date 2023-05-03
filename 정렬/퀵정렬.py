# 숫자를 입력 받아 오름차순
# 입력
"""
10 
1 4 3 2 5 9 8 6 7 10
"""

import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

# 퀵정렬
print("---------퀵정렬----------")


def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    low = start + 1
    high = end
    while low < high:
        while True:
            if low > end or array[low] > array[pivot]:
                break
            else:
                low += 1

        while True:
            if high < start + 1 or array[high] < array[pivot]:
                break
            else:
                high -= 1
        if low > high:
            array[high], array[pivot] = array[pivot], array[high]
            break
        else:
            array[high], array[low] = array[low], array[high]
    quick_sort(array, 0, high - 1)
    quick_sort(array, high + 1, end)


quick_sort(num_list, 0, len(num_list) - 1)

for i in num_list:
    print(i, end=" ")
