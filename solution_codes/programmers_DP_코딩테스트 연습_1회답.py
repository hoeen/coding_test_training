# 코딩 테스트 공부
# 박우석
def solution(alp, cop, problems):
    # DP - bottom-up
    max_algo = max([p[0] for p in problems])
    max_code = max([p[1] for p in problems])
    
    if alp >= max_algo and cop >= max_code:
        return 0

    dp_tab = [[int(1e9)]*(max_code+1) for _ in range(max_algo+1)] 
    dp_tab[min(alp, max_algo)][min(cop, max_code)] = 0
    
    for a in range(alp, max(alp, max_algo)+1):
        for c in range(cop, max(cop, max_code)+1):
            
            if a > max_algo:
                a = max_algo
            if c > max_code:
                c = max_code
            
            if a+1 <= max_algo:
                dp_tab[a+1][c] = min(dp_tab[a+1][c], dp_tab[a][c] + 1)
            
            if c+1 <= max_code:
                dp_tab[a][c+1] = min(dp_tab[a][c+1], dp_tab[a][c] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req: # 풀수있는 문제
                    
                    a_with_rwd = min(a + alp_rwd, max_algo)
                    c_with_rwd = min(c + cop_rwd, max_code)
                    
                    dp_tab[a_with_rwd][c_with_rwd] = min(dp_tab[a_with_rwd][c_with_rwd], 
                                                            dp_tab[a][c] + cost)
    
    return dp_tab[max_algo][max_code]