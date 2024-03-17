import sys

n = int(sys.stdin.readline())

commands_all = []
for i in range(n):
    commands_all.append(sys.stdin.readline())


def gogoTurtle(commands):
    now_x = 0
    now_y = 0
    now_way = 'up'

    max_x = 0
    min_x = 0

    max_y = 0
    min_y = 0

    list(commands)
    for c in commands:
        if c == "F":
            if now_way == 'up':
                now_y += 1
            elif now_way == 'down':
                now_y -= 1
            elif now_way == 'right':
                now_x += 1
            elif now_way == 'left':
                now_x -= 1
            # 최댓값 체크
            if now_x > max_x:
                max_x = now_x
            elif now_x < min_x:
                min_x = now_x
            elif now_y > max_y:
                max_y = now_y
            elif now_y < min_y:
                min_y = now_y
        elif c == "B":
            if now_way == 'up':
                now_y -= 1
            elif now_way == 'down':
                now_y += 1
            elif now_way == 'right':
                now_x -= 1
            elif now_way == 'left':
                now_x += 1
            # 최댓값 체크
            if now_x > max_x:
                max_x = now_x
            elif now_x < min_x:
                min_x = now_x
            elif now_y > max_y:
                max_y = now_y
            elif now_y < min_y:
                min_y = now_y
        elif c == "L":
            if now_way == 'up':
                now_way = "left"
            elif now_way == 'left':
                now_way = "down"
            elif now_way == 'down':
                now_way = "right"
            elif now_way == 'right':
                now_way = "up"
        elif c == "R":
            if now_way == 'up':
                now_way = "right"
            elif now_way == 'right':
                now_way = "down"
            elif now_way == 'down':
                now_way = "left"
            elif now_way == 'left':
                now_way = "up"
    print((max_x - min_x)*(max_y - min_y))


for commands in commands_all:
    gogoTurtle(commands)
