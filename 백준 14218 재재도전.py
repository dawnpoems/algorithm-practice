import sys

city_num, road_num = map(int, sys.stdin.readline().split())
road_list_now = []

for i in range(road_num):
    road_list_now.append(list(map(int, sys.stdin.readline().split())))

plan_num = int(sys.stdin.readline())

road_list_plan = []
for i in range(plan_num):
    road_list_plan.append(list(map(int, sys.stdin.readline().split())))




for i in road_list_plan:
    # 하나 추가됐을 때 최소, 그다음 그다음~~
    road_list_now.append(i)
    

    print(' '.join(map(str, min_distance)))
