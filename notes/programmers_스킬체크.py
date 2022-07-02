import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0] < K:
        if len(scoville) == 2 and min(scoville) + 2*max(scoville) < K:
            return -1
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        s_new = s1 + (s2*2)
        heapq.heappush(scoville, s_new)
        answer += 1
    return answer


# def solution(scoville, K):
# answer = 0
# scoville.sort()
# while scoville[0] < K:
#     if len(scoville) == 2 and scoville[0] + 2*scoville[1] < K:
#         return -1
#     s1 = scoville.pop(0)
#     s2 = scoville.pop(0)
#     s_new = s1 + (s2*2)
#     scoville.insert(0,s_new)
#     scoville.sort()
#     answer += 1
# return answer