from collections import defaultdict
from math import ceil

def solution(fees, records):

    btime, bcost, utime, ucost = fees # 기본시간, 기본요금, 단위시간, 단위요금
 
    '''
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
			"07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
			"19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    '''
    # 누적 주차시간 계산
    costs = defaultdict(int) # 누적시간
    times = {}
    for rec in records:
        t, num, st = rec.split()
        hour, minute = t[:2], t[3:]
        if st == 'IN':
            # 입차 - 시각 남겨둠
            times[num] = [int(hour), int(minute)]
        else:
            # 출차 - 입차시각과 차 구해서 주차시간 기억
            ent_hour, ent_minute = times[num]
            # 누적시간을 분으로 갱신
            costs[num] += ((int(hour) - ent_hour)*60 + (int(minute) - ent_minute))
            # 출차했으면 입차를 없앰
            del times[num]
    # 남아있는 입차시간을 23:59에서 빼서 누적시간 더함
    for car in times:
        ent_hour, ent_minute = times[car]
        costs[car] += ((23 - ent_hour)*60 + (59 - ent_minute))
    
    prices = []
    for cnum, elapsed in costs.items():
        
        prices.append(
            (
            cnum, 
            bcost + ceil(max(elapsed - btime, 0) / utime) * ucost)
            )
    
        
    prices.sort(key = lambda x: x[0])
    
    
    # 차량 번호가 작은 자동차부터 청구할 주차 요금
    return [p[1] for p in prices]