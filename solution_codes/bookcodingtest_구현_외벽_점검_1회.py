from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # weak 길이 늘리기
    for w in range(length):
        weak.append(n+weak[w])
    cand = []
    for start in range(length): # 각 weak point를 출발점으로 설정
        # 끝점 설정        
        
        for friends in list(permutations(dist, len(dist))):
            pos = weak[start] # 첫 출발지점
            count = 1
            for friend in friends:
                fr_dist = pos+friend
                if fr_dist < weak[start+length-1]: # 끝점이란? 시작점부터 마지막 weak까지의 거리
                    count += 1 # 친구 추가
                    pos = [i for i in weak if i > fr_dist][0] # 다음 취약지점부터 시작
                
                else: # 끝점 도달
                    cand.append(count)
            # print('friends:', friends)
            # print('count:', count)
    return min(cand) if cand else -1

print(solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4]))
print(solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7]))