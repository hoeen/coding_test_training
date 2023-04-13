def solution(n, s, a, b, fares):
    
    # 제한사항 : 지점 200개 이하
    # 200*200*200 = 6000000 -> 플로이드 가능
    
    # 플로이드 워셜 - 1~n까지
    INF = int(1e9)
    dp = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 0
    for x, y, cost in fares:
        dp[x][y] = cost
        dp[y][x] = cost
    
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                dp[x][y] = min(dp[x][y], dp[x][k] + dp[k][y])
                
    # 모든 최단거리가 구해짐.
    # A-B 가 같이 이동함 -> 따로 이동
    # 같이 가는 노드를 모든 경우에서 구해봄
    # S -> K (같이) 
    # K -> A
    # K -> B (따로)
    min_fare = int(1e9)
    for mid in range(1, n+1):
        fare = dp[s][mid] + dp[mid][a] + dp[mid][b]
        if min_fare > fare:
            min_fare = fare
        
    return min_fare