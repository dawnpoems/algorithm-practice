import sys
input = sys.stdin.readline

n, m, ivt = map(int, input().split())

ground_list = []
for _ in range(n):
    ground_list.append([int(x) for x in sys.stdin.readline().rstrip().split()])

min_num = min(map(min, ground_list))
max_num= max(map(max, ground_list))

min_time = int(1e9)
min_ground = 256

for i in range(min_num, max_num + 1) :
    take_block = 0
    use_block = 0
    for j in range(n) :
        for k in range(m) :
            if ground_list[j][k] > i :
                take_block += ground_list[j][k] - i
            else : 
                use_block += i - ground_list[j][k]
            

    if use_block > take_block + ivt:
        continue

    time = take_block*2 + use_block

    if time <= min_time :
        min_time = time
        min_ground = i

print(min_time, min_ground)