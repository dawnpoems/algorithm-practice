import sys

input = sys.stdin.readline

n = int(input())

tri = []
road = [[] for _ in range(n)]

for i in range(n):
    tri.append(list(map(int, input().split())))


road[0].append(tri[0][0])

for floor in range(1, n):
    for index in range(floor + 1):
        if index <= 0:
            road[floor].append(road[floor-1][index] + tri[floor][index])
        elif index >= floor:
            road[floor].append(road[floor-1][index-1] + tri[floor][index])
        else:
            road[floor].append(
                max(road[floor-1][index-1], road[floor-1][index]) + tri[floor][index])

print(max(road[-1]))

# 존재한다면? 위층의 n값과 n-1값중에 큰거 + 내꺼가 현재값
