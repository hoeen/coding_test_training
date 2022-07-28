# ~ 12:00
import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
seq = [tuple(map(int, input().split())) for _ in range(n)]  # (무게, 가격) ]

bags = [int(input()) for _ in range(k)]

'''
가장 무게 작은 용량의 가방부터
무게 같거나 작은 보석들을 heap에 가격을 집어넣는다 (보석은 무게순)
이때 같은 가격이면 무게 무거운것부터 넣어주어야 가장 무거운 것이 처음으로 오게됨.
즉 사전에 보석을 무거운것부터 정렬해 주어야 함
그리고 heap에서 pop하면 가장 가격 높고, 무거운것이 탐색할 필요없이 처음으로 딱 나온다.
'''

# 무게 큰것 순으로 정렬. 가격은 heap 인덱스로 넣으므로 정렬 필요없음.
seq.sort() # 무게 오름차순으로 정렬
bags.sort() # 가방도 오름차순으로 정렬

# print('check queue')
# print(q)
total = 0
temp = []
for i in range(k):
    bag = bags[i]
    # print('bag weight:', bag)
    while seq and bag >= seq[0][0]: # 무게
        weight, price = heapq.heappop(seq)
        # print(weight, price)
        heapq.heappush(temp, -price) # 음수로 넣으면 heappop 시 최댓값부터 -로 반환시킴
    # print(temp, seq)
    if temp:
        total -= heapq.heappop(temp)
    elif not seq:
        break

print(total)

