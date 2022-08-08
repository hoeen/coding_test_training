import heapq

def solution(jobs):
    '''
    요청부터 종료까지 시간 총합이 최소가 되도록 -> 평균 반환
    소요시간 작은것부터 처리하면 되지 않을까?
    0, 3 / 1, 9 / 2, 6 
    요청부터 종료까지가 최소한으로 되도록 해야함.
    
    '''
    q = []
    jobs.sort(key = lambda x: (x[0], x[1])) # 시점 빠른 순으로 정렬
    print(jobs)
    n = len(jobs)
    # 시간 순으로 우선 정렬하고, 밀린 작업들을 heap에 넣었다가 elap 순으로 빼자.
    now = 0
    total = 0
    
    # 맨 처음 작업 우선 실행. 
    start, elap = jobs.pop(0)
    now = start + elap
    total += elap
    
    print('start')
    print(now, total)
    while jobs:
        start, elap = jobs.pop(0) # 다음 작업 꺼내기
        print('next job:', start, elap)
        if start < now: # 다음 요청시간이 now보다 이전이면
            print('push')
            print(elap, start)
            heapq.heappush(q, (elap, start)) # heapq에 집어넣기
            
        else:#if start >= now or not jobs: # 다음 꺼낸 요청이 delay 안생기면 또는 마지막 작업이면 : 우선 heapq에 있는것부터 처리하면서 시간 갱신
            while q:
                q_elap, q_start = heapq.heappop(q)
                print('heappop')
                print(q_elap, q_start)
                delay = now - q_start
                total += (delay + q_elap)
                now += q_elap
                print('delay, total, now')
                print(delay, total, now)
                
            # 만약 마지막 요청이면 시간갱신하고 종료.
            if not jobs:
                if start < now:
                    delay = now - start
                else:
                    delay = 0

                total += (delay + elap)

                print('last')
                print('delay, total')
                print(delay, total)
                return int(total / n)
                
            else:   
            # 마지막 요청 아니고 heapq 처리후에 꺼냈던 요청이 delay 생기면, 다시 jobs 집어넣고 loop
                if start < now and jobs:
                    jobs.insert(0, (start, elap))
                else: # 그래도 delay 안생기면 시간 갱신하고 loop
                    print('not delayed')
                    total += elap
                    now = start + elap