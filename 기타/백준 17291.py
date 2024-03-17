import sys
from collections import deque

n = int(sys.stdin.readline())
holsu = False

new_bulles = deque([1])
# 짝수년도, 4번 분열시 사망,
# 홀수년도, 3번 분열시 사망.
# 1년에 태어난 애는 4년 1월에 분열하고 사망
# 2년, 3년에 태어난 애는 동일하게 6년에 사망 ....
# 4년 5년은 8년...
for i in range(2, n+1):
    new_bulles.append(sum(new_bulles))
    if i == 2:
        continue
    elif i == 4:
        new_bulles.popleft()
    elif i % 2 == 0:
        new_bulles.popleft()
        new_bulles.popleft()

all_bulles = 0
for i in new_bulles:
    all_bulles += i

print(all_bulles)
