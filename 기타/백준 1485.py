import sys, math
input = sys.stdin.readline

T = int(input())

def get_distance(x1, y1, x2, y2) :
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

for t in range(T) :
    dots = []
    for i in range(4) :
        dots.append(tuple(map(int, input().split())))
    dists = []
    dists.append(get_distance(dots[0][0], dots[0][1], dots[1][0], dots[1][1]))
    dists.append(get_distance(dots[0][0], dots[0][1], dots[2][0], dots[2][1]))
    dists.append(get_distance(dots[0][0], dots[0][1], dots[3][0], dots[3][1]))
    dists.append(get_distance(dots[1][0], dots[1][1], dots[2][0], dots[2][1]))
    dists.append(get_distance(dots[1][0], dots[1][1], dots[3][0], dots[3][1]))
    dists.append(get_distance(dots[2][0], dots[2][1], dots[3][0], dots[3][1]))
    uniq_dists = set(dists)
    
    if len(uniq_dists) != 2 :
        print(0)
        continue
    side = min(uniq_dists)
    side_cnt = 0
    for di in dists :
        if di == side :
            side_cnt += 1
    
    
    if side_cnt == 4 :
        print(1)
    else :
        print(0)
    