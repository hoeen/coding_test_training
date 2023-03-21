# ~ 11:00
def solution(s):
    answer = len(s)
    # 압축길이 : 최대가 s//2
    # 완탐 경우 - 2 ~ 500 
    for l in range(1, len(s)//2+1):
        comp = ''
        count = 1
        for i in range(0, len(s)//l):
            if i == 0:
                before = s[:l]
            else:
                after = s[i*l : (i+1)*l] # l만큼 자름
                if before == after:
                    count += 1
                    
                    if i == len(s)//l-1:
                        comp += (str(count) + before)
                        
                else: # 달라질때
                    if count > 1:
                        comp += (str(count) + before)
                    else:
                        comp += before
                    before = after # after로 before를 치환
                    count = 1
                    
                    if i == len(s)//l-1:
                        comp += after

        comp += s[(i+1)*l:]
        if answer > len(comp):
            answer = len(comp)
                
    
    return answer