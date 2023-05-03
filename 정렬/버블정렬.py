# 숫자를 입력 받아 오름차순
# 입력
"""
10 
1 4 3 2 5 9 8 6 7 10
"""

import sys
n = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

# 버블정렬
print("---------버블정렬----------")

for i in range(len(num_list) - 1, 1, -1):
    for j in range(i):
        if num_list[j] > num_list[j + 1]:
            num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

for i in num_list:
    print(i, end=" ")
