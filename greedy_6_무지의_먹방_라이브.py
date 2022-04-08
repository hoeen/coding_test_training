'''
1~N까지 음식이 있음
N음식 먹으면 다시 1번음식이 온다
1초동안 먹고 남기고 다음음식 먹음
food_times에 각 음식별 소요시간이 들어있다.
[3,1,2]
'''

k = int(input())
food_times = list(map(int, input().split()))


order = 0
    
for _ in range(k):
    
    while food_times[order] == 0:
        order += 1
        if order > len(food_times):
            print(-1)
    
    food_times[order] -= 1
    order += 1
    
    # 회전 구현 - food_times개수를 order이 넘어가면 다시 0
    if order == len(food_times):
        order = 0
    print(food_times)

print((order + 1) % len(food_times))


        

    # 다먹은 음식도 순서 있으므로 남겨두어야한다. 0이면 그냥 그다음꺼 먹기