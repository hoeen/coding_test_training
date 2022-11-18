# 13:00 시작
n, m, l = map(int, input().split())

loc = list(map(int ,input().split()))

start = 0
end = l

# 남아 있는 휴게소 중




# m개 휴게소 짓고 나서 휴게소 없는 구간 최댓값이 최소가 되도록. 이를 출력
loc.sort()
# 처음과 끝점 추가
loc.insert(0,0)
loc.append(l)
rests = m



# 최대간격을 d로 했을 때 몇개까지 지어지나 보기.
# m개보다 더 지을 수 있으면 - > d 를키움
# m개보다 적으면 -> d를 줄임
# d 초기값: 간격중 최댓값
# max_dist = 0
# for i in range(len(loc)-1):
#     # 맨처음과 휴게소 거리
#     dist = loc[i+1] - loc[i]
#     if max_dist < dist:
#         max_dist = dist
max_dist = l

def binary_search(array, value, start, end):
    if start > end:
        return
    else:
        mid = (start + end) // 2
        # mid 를 최대 길이로 가질 때 몇 개까지 지을 수 있나?


binary_search(array, m, 0, max_dist)



#
# while rests > 0:
#     dists = []
#     max_dist = 0
#     max_loc = None
#
#     # 전체 간격 측정하고 최대 간격을 찾음
#     for i in range(len(loc)-1):
#         # 맨처음과 휴게소 거리
#         dist = loc[i+1] - loc[i]
#         if max_dist < dist:
#             max_dist = dist
#             max_loc = i   # i ~ i+1 이 간격 최대임
#         dists.append(dist)
#     print('measured dists:', dists)
#
#     # 최대 간격 중간에 하나 지어서 1/2로 만듬. 중간이 없으면 왼쪽에 짓기
#     mid = (loc[max_loc] + loc[max_loc+1]) // 2
#     loc.append(mid)
#     loc.sort()
#     print('new loc:', mid)
#     print('updated loc:', loc)
#     # 지을 휴게소 수 하나 빼기
#     rests -= 1
#
# total_max_dist = None
# for i in range(len(loc)-1):
#     dist = loc[i+1] - loc[i]
#     if total_max_dist is None:
#         total_max_dist = dist
#     if total_max_dist < dist:
#         total_max_dist = dist
#
# print(total_max_dist)

