import sys
from collections import deque
input = sys.stdin.readline

for i in range(int(input())) :
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    queue = deque(li)
    imps = list(set(li))

    imps.sort()
    # print(imps)
    # print(queue)

    cnt = 0
    p = m
    end_flag = False

    target = imps.pop()
    # print("-----")

    while queue : #queue가 완전히 없어질 때까지
        if target not in queue :
            target = imps.pop()
        now = queue.popleft() #첫 번째 확인
        p -= 1 #p위치 재조정
        if p < 0 :
            p = len(queue)

        if now == target : #인쇄 타이밍이면
            cnt += 1 #인쇄
            if p == len(queue) : #지금것이 알고싶은 앤지 확인
                print(cnt)
                break
        else : #인쇄 타이밍 아니면 돌려놓기
            queue.append(now)
    #     print(target, end=" | ")
    #     print(p, end=" | ")
    #     print(queue)

    # print("-------")
        
