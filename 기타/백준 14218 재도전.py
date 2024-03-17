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

for i in range(2, city_num+1):
    unchecked_list.append(i)

# 한번 돌리고
# 남은 걸로 또 한번 돌리고
# 남은걸로 또 한번 돌리고
# 안남을 때까지
# 재귀?


def hihi(node_list, count):
    if len(node_list) <= 0:
        return
    linked_list = []
    count += 1
    for node in node_list:
        for road in road_list_now:
            if node in road:
                if road[0] == node:
                    c = road[1]
                else:
                    c = road[0]  # node가 아닌것을 가져와야 함.

                print(min_distance)
                min_distance[c - 1] = count
                if c in unchecked_list:
                    linked_list.append(c)
                    unchecked_list.remove(c)

    print("-------------------")
    print(linked_list)
    hihi(linked_list, count)
# count 0으로 시작
# 처음에는 1만 들은 리스트로 시작
# linked_list초기화
# 카운트 하나 시작.
# 전체 node_list로 for문.
# 연결된 것이 있는지 확인(road_list_now) for문. 1번과 연결된 것이 있는가? 2번
# 연결된 경우에는 min_distance를 count로 변경
# unchecked_list에 있으면, linked_list로 추가, 추가하는 순간 unchecked_list에서 삭제
# new_linked_list로 함수 다시 시작
# new_linked_list가 없는순간 종료.(있을때만 while)


for i in road_list_plan:
    # 하나 추가됐을 때 최소, 그다음 그다음~~
    road_list_now.append(i)
    min_distance = []
    for i in range(0, city_num):
        # 기본은 못가는걸로 세팅
        min_distance.append(-1)
        min_distance[0] = 0

    hihi([1], 0)

    print(' '.join(map(str, min_distance)))
