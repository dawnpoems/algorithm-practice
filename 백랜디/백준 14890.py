import sys
input = sys.stdin.readline

N, L = map(int, input().split())

board = []

ans = 0
def is_road(line) :
    prev = line[0]
    i = 1
    slope = [False] * N
    # print("----------------")
    while i < N :
        # print(slope)
        now = line[i]
        # print(i, prev, now)
        if prev != now :
            if abs(prev - now) > 1 :
                return False
            
            # 올라가는 슬로프      
            if prev < now :
                #2개 슬로프를 놓으려면 커진 곳이 인덱스 2는 되어야 함.
                if i < L :
                    return False
                b = 1
                while b <= L :
                    if line[i - b] != prev or slope[i - b] == True :
                        return False
                    b += 1
                while b > 1:
                    b -= 1
                    slope[i - b] = True
            # 내려가는 슬로프
            else :
                if i + L > N :
                    return False
                b = 1
                while b < L :
                    # print(b)
                    if line[i + b] != now :
                        return False
                    b += 1
                i += b - 1
                now = line[i]
                while b :
                    b -= 1
                    slope[i - b] = True
        prev = now
        i += 1
    return True

for i in range(N) :
    line = list(map(int, input().split()))
    if is_road(line) :
        # print("row : ", i)
        ans += 1
    board.append(line)

for i in range(N) :
    line = []
    for j in range(N) :
        line.append(board[j][i])
    if is_road(line) :
        # print("col : ", i)
        ans += 1

# line = []
# for j in range(N) :
#     line.append(board[j][0])
# if is_road(line) :
#     print("col : ", i)
#     ans += 1

print(ans)