# 집합으로 풀이 - 이긴 경우, 진 경우
def solution(n, results):
    wins = [set() for _ in range(n+1)]
    loses = [set() for _ in range(n+1)]
    for w, l in results:
        wins[w].add(l) # 어떤 팀을 이겼는지
        loses[l].add(w) # 어떤 팀한테 졌는지
        
    # 이기면 그동안 상대 팀이 이긴 전적 가져오고
    # 지면 그동안 상대 팀이 진 전적 가져오기
    # O(n^2)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if j in wins[i] or i in loses[j]: # i가 j 이김
                wins[i].update(wins[j])
                loses[j].update(loses[i])
            elif i in wins[j] or j in loses[i]: # j가 i 이김
                wins[j].update(wins[i])
                loses[i].update(loses[j])
    answer = 0
    for k in range(1, n+1):
        if len(wins[k]) + len(loses[k]) == n-1:
            answer += 1
    
    return answer