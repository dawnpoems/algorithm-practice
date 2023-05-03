# 숫자를 입력 받아 오름차순
# 입력
"""
10 
1 4 3 2 5 9 8 6 7 10
"""

import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))


# 선택정렬,
# 0~4, 1~4, 2~4
print()
print("---------선택정렬----------")

for i in range(len(num_list) - 1):
    min_index = i
    for j in range(i, len(num_list)):
        if num_list[j] < num_list[min_index]:
            min_index = j
    num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

for i in num_list:
    print(i, end=" ")
