import sys
input = sys.stdin.readline

T = int(input())

for t in range(T) :
    N = int(input())
    meals = list(map(int, input().split()))
    day = 1
    while sum(meals) <= N :
        nx_meals = []
        for i in range(6) :
            left = i - 1
            right = i + 1
            if right > 5 :
                right -= 6
            front = i - 3
            nx_meals.append(meals[i] + meals[left] + meals[right] + meals[front])
        meals = nx_meals
        day += 1
    print(day)