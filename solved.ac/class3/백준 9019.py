from collections import deque
import sys
input = sys.stdin.readline

def D_exec(n) :
    ret = n * 2
    if (ret > 9999) :
        ret = ret % 10000
    return ret

def S_exec(n) : 
    if (n == 0) :
        return 9999
    return n - 1

def L_exec(n) :
    thou = n // 1000
    hund = (n % 1000) // 100
    ten = (n % 100) // 10
    one = n % 10
    ret = 0
    ret += hund * 1000
    ret += ten * 100
    ret += one * 10
    ret += thou
    return ret

def R_exec(n) :
    thou = n // 1000
    hund = (n % 1000) // 100
    ten = (n % 100) // 10
    one = n % 10
    ret = 0
    ret += one * 1000
    ret += thou * 100
    ret += hund * 10
    ret += ten
    return ret

T = int(input())

def find_road_and_print(end, A) :
    road = deque([])
    now = end
    while now != A :
        road.append(now)
        now = visited[now]
    road.append(A)
    # print(road)
    before = road.pop()
    while road :
        after = road.pop()
        if D_exec(before) == after :
            print("D", end="")
        elif S_exec(before) == after :
            print("S", end="")
        elif L_exec(before) == after :
            print("L", end="")
        elif R_exec(before) == after :
            print("R", end="")
        before = after
    print()

for t in range(T) :
    A, B = map(int, input().split())
    queue = deque([])
    visited = [-1] * 10000
    queue.append([D_exec(A), A])
    queue.append([S_exec(A), A])
    queue.append([L_exec(A), A])
    queue.append([R_exec(A), A])
    while queue :
        now = queue.popleft()
        if visited[now[0]] != -1 :
            continue
        visited[now[0]] = now[1]
        if B == now[0] :
            find_road_and_print(now[0], A)
            break
        queue.append([D_exec(now[0]), now[0]])
        queue.append([S_exec(now[0]), now[0]])
        queue.append([L_exec(now[0]), now[0]])
        queue.append([R_exec(now[0]), now[0]])