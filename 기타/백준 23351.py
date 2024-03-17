import sys
n, k, a, b = map(int, sys.stdin.readline().split())

list = []
day = 0
for i in range(n//a):  # 어차피 n/a개 단위로 주고, a는 n의 약수로만 주어지므로
    list.append(k)  # 앞에서부터 하나씩 물 주는걸로 단순화

while True:
    day += 1  # 날짜가 하루씩 지나감
    list[day % (n//a)] += b  # 앞에서부터 돌아가면서 하나씩 물줌
    for i in range(len(list)):  # 리스트의 모든 값 -1
        list[i] -= 1

    if min(list) <= 0:  # 최솟값이 0이면 반복문 종료
        break

print(day)
