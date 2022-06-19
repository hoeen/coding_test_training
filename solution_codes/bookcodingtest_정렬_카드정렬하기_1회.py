# ~11:00
import heapq

n = int(input())
decks = []
for _ in range(n):
    heapq.heappush(decks, int(input()))

answer = 0
while len(decks) > 1:
    a = heapq.heappop(decks)
    b = heapq.heappop(decks)
    heapq.heappush(decks, a+b)
    answer += (a+b)

print(answer)



