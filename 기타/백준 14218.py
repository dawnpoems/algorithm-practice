import sys

city_num, road_num = map(int, sys.stdin.readline().split())
road_list_now = []

for i in range(road_num):
    road_list_now.append(list(map(int, sys.stdin.readline().split())))

plan_num = int(sys.stdin.readline())

road_list_plan = []
for i in range(plan_num):
    road_list_plan.append(list(map(int, sys.stdin.readline().split())))

unchecked_list = []

min_distance = []
for i in range(1, city_num+1):
    # 기본은 못가는걸로 세팅
    unchecked_list.append(i)
    min_distance.append(-1)
    min_distance[0] = 0

# 한번 돌리고
# 남은 걸로 또 한번 돌리고
# 남은걸로 또 한번 돌리고
# 안남을 때까지
# 재귀?
count = 0

linked_list = []

for i in road_list_plan:
    # 하나 추가됐을 때 최소, 그다음 그다음~~
    road_list_now.append(i)

    # 여기서 최솟값 구해서 합치기
    while len(unchecked_list) > 0:
        if 1 in unchecked_list:
            unchecked_list.remove(1)
        for node in unchecked_list:
            count += 1
            for road in road_list_now:
                if node in road:
                    road.remove(node)  # road에서 node를 빼버리고 남은건, node와 연결된 숫자
                    min_distance[road[0] - 1] = count
                    if road[0] not in linked_list:
                        linked_list.append(road[0])

    print(' '.join(map(str, min_distance)))

# 전체 리스트에서 방문한 곳은 빼
# 오히려 확인한 곳 리스트에는 넣어
# 연결 안된 위치도 따로 저장
# 거리 +1 한 상태에서 방금 확인한 곳과 연결되는 곳이 있는지 확인

# 이걸 언제까지 반복? 모든 노드를 확인할 때까지
