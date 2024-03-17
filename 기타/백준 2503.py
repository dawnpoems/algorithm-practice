import sys
n = int(sys.stdin.readline())

num_list = []
strike_ball = []

for i in range(n):
    num, strike, ball = sys.stdin.readline().split()
    num_list.append(list(map(int, list(num))))
    strike_ball.append(list(map(int, [strike, ball])))

print(num_list)
print(strike_ball)

possiblity = []

for i in range(1, 10) :
    for j in range(1, 10) :
        for z in range(1, 10) :
            possiblity.append([i, j, z])


for i in range(len(strike_ball)) :
    if strike_ball[i][0] == 0 :
        continue
    elif strike_ball[i][0] == 1 :
        for j in possiblity :





