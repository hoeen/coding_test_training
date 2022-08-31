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

# 플로이드 워셜 이용한 풀이
def solution(n, results):
    board = [[0]*(n+1) for _ in range(n+1)]
    for w, l in results:
        board[w][l] = 1 # w가 l 이김
        board[l][w] = -1 # l은 w한테 짐
    # 플로이드 워셜 알고리즘 - k, a, b 순서 중요. 
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                # 양수이면 관계 파악 가능, 음수 혹은 0이면 불가능
                if board[x][k] * board[k][y] > 0: # 지고 지거나 이기고 이기면 확인됨
                    board[x][y] = board[x][k]
    answer = 0
    for i in range(1, n+1):
        if board[i][1:].count(0) == 1:
            answer += 1
            
    return answer