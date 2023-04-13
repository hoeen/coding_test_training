from heapq import heapify, heappop, heappush

def solution(scoville, K):
    
    count = 0
    # 불가능 경우 처리하기
    heapify(scoville) # 최소 - 최대
    # for _ in range(int(1e6)):
    while True:
        dish1 = heappop(scoville)
        # K 체크
        if dish1 >= K:
            return count
        # 큐 비어있으면 -1 리턴
        if not scoville: return -1
        dish2 = heappop(scoville)
        mix = dish1 + (dish2*2)
        heappush(scoville, mix)
        count += 1