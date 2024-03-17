import sys
n = int(sys.stdin.readline())

for i in range(n):
    score_list = []
    count = 0
    num = int(sys.stdin.readline())
    for j in range(num):
        count += 1
        score = list(map(int, sys.stdin.readline().split()))
        score_list.append(score)

    score_list.sort(key=lambda x: x[0], reverse=True)
    # 자기 다음에 나오는 것 중에
    # 자기보다 등수가 높은(숫자가 작은) 숫자가 하나라도 있다면
    # 그 사람은 못뽑음.
    print(score_list)
    high_rank = score_list.pop()[1]
    while len(score_list) >= 1:
        tmp_rank = score_list.pop()[1]
        print(high_rank)
        if tmp_rank < high_rank:  # 다음게 등수가 낮으면
            high_rank = tmp_rank  # 가장 높은 등수 다시 재배치.
        else:
            count -= 1  # 얜 못씀.

    print(count)
