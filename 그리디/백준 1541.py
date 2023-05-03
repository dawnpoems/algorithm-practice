# 마이너스 기준으로 split
# 처음 값은 디폴트
# 다음 값부터 +로 나눠서 전부 더하기
# 더한 값만큼 싹 빼기.

import sys
input = sys.stdin.readline

plused = []

mi_list = list(input().split("-"))
for i in mi_list:
    plused_cnt = 0
    pu_list = i.split("+")
    for j in pu_list:
        plused_cnt += int(j)
    plused.append(plused_cnt)

total = 0

total += int(plused.pop(0))

if len(plused) > 0:
    for k in plused:
        total -= int(k)

print(total)
