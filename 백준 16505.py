import sys
n = int(sys.stdin.readline())

if n == 0:  # 0이면 그냥 별 하나 출력하고 종료
    print("*")
count = 1

stars = ["*"]

while n >= 1:
    if count >= n:  # count랑 n이 같아지면 반복문 종료
        for i in stars:
            print((i + i).rstrip())  # 쓸모없는 공백은 제거
        for i in stars:
            print(i.rstrip())
        break

    new_stars = []  # 새로운 리스트 매번 만듦
    for i in stars:  # 이전 리스트 전체만큼 순회
        new_stars.append(i+i)  # 이전 리스트들 전부 두번 반복
    for i in stars:  # 처음은 그대로, 나머지는 i만큼의 공백만 더하기
        new_stars.append(i + i.replace("*", " "))
    count += 1
    stars = new_stars


# 다음은 위층 처음꺼 + 처음꺼
# 처음꺼 + 빈칸

# 이걸 리스트로 어케 구현하지...
# 층수별로 찍는다고 치면
# 저장이 어떻게 되어 있어야..?
# ["****", "* * ", "**", "*" ] 이렇게 되어있다고 치면
# 리스트 전체 순회
# 1번 + 1번,/ 2번 + 2번.rstrip, / 3번 + 3번.rstrip / 4번 + 4번.rstrip()
# 1번, 2번, 3번, 4번
# 다음번 리스트에 저장은?
# 리스트 비우고, 새로 찍을 때마다 저장.
