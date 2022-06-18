import heapq

food_times = [3,1,2,4,5,7,8,6]
k = 15

# 남은시간, 음식번호 로 heap에 추가

# greedy 방법
# 가장 작은 시간 가진것부터 불러서, k - len(food_times)*남은시간 함
# 만약 k가 더 작을경우: 남은것들 다시 나열해서 불러오면됨
# 스킵하는 방법을 인덱싱할 필요가 없다. 겁나 간단하네..
if sum(food_times) <= k:
    print(-1)

heap = []
for i in range(len(food_times)):
    heapq.heappush(heap,(food_times[i],i+1)) # 남은시간, 음식번호
    

elapsed = 0 # 돈 바퀴 (먹은수)
while heap:
    food_len = len(heap)
    time, number = heapq.heappop(heap)
    # 뽑아낸 time에서 현재 돈 바퀴만큼을 뺀다
    time -= elapsed
    # 남은음식수 * 빼고남은 time이 k보다 작으면 다먹는거고
    if food_len*time < k:
        k -= food_len*time
        elapsed += time

        
    # k보다 크면 셈을 한다
    else:
        # 뺀거 다시 집어넣음
        heapq.heappush(heap,(time,number))
        # 정렬 리스트
        heap = sorted(heap,key=lambda x: x[1])
        
        goal = heap[k%food_len]
        # 목표의 숫자를 출력
        print(goal[1])
        break




