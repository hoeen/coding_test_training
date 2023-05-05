import heapq

n = int(input()) # 2~100000

liq = list(map(int, input().split()))
liq.sort()

lp, rp = 0, n-1
cand = []
min_ = 1<<100
while lp < rp:
    sum_ = liq[lp] + liq[rp]
    if min_ > abs(sum_):
        min_ = abs(sum_)
        heapq.heappush(cand, (abs(sum_), (liq[lp], liq[rp]))) 
    if sum_ == 0:
        break
    elif sum_ < 0:
        lp += 1
    elif sum_ > 0:
        rp -= 1

print(*heapq.heappop(cand)[1])
