from collections import deque

def solution(pro, spd):
    answer = []
    comp = deque([])
    qpro = deque(pro)
    qspd = deque(spd)
    p = qpro.popleft()
    s = qspd.popleft()
    total_date = (100 - p) // s  # 며칠후에 배포가능
    if (100 - p) % s > 0: 
        total_date += 1 # 안맞아떨어지면 하루 추가
    
    comp.append(p)
    
    while qpro:
        qp = qpro.popleft()
        qs = qspd.popleft()
        
        due_date = (100 - qp) // qs
        if (100 - qp) % qs > 0:
            due_date += 1
   
        if total_date >= due_date: 
            # 다음 작업 기간이 총진행일보다 같거나 일찍끝남
            comp.append(qp)
            if not qpro:
                answer.append(len(comp))
                break
        else: # 다음작업이 더걸림 - 앞선것을 배포
            answer.append(len(comp)) # 배포
            comp = deque([])
            total_date = due_date
            if not qpro:
                answer.append(1)
                break
            else:
                qpro.appendleft(qp)
                qspd.appendleft(qs)
        
    return answer