import sys
input = sys.stdin.readline

def find_area(idx, start, end) :
    area = blocks[idx]
    left = idx
    right = idx
    width = 1
    height = blocks[idx]
    while left > start or right < end :
        if right >= end or (left - 1 >= start and blocks[left - 1] >= blocks[right + 1]) :
            left -= 1
            height = min(height, blocks[left])
        else :
            right += 1
            height = min(height, blocks[right])
        width += 1
        area = max(area, width * height)
    return area

def div_and_conq(start, end) :
    if start == end :
        return blocks[start]
    elif end - start == 1 :
        if blocks[start] < blocks[end] :
            return max(blocks[end], blocks[start] * 2)
        else :
            return max(blocks[start], blocks[end] * 2)
    mid = (start + end) // 2
    return max(find_area(mid, start, end), div_and_conq(start, mid), div_and_conq(mid + 1, end))

while True :
    line = list(map(int, input().split()))
    N = line[0]
    if line[0] == 0 :
        break
    blocks = []
    for i in range(1, N + 1) :
        blocks.append(line[i])
    
    print(div_and_conq(0, N - 1))