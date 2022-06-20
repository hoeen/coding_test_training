from collections import deque

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cost = [0] * (n+1)


# 소요시간, 
for j in range(1, n+1):
    inp = list(map(int, input().split()))
    for i in range(len(inp)): 
        if i == 0: # j과목의 소요시간
            cost[j] = inp[i]
        elif inp[i] != -1: # j과목의 선수과목
            prior = inp[i]
            graph[prior].append(j)
            indegree[j] += 1
# 동시에 여러 강의 수강 가능         
# n까지의 최소시간 어떻게 계산?
# 같은 length로 들어간 큐에서, 최소시간만 고려한다.

# 위상 정렬 함수
def topology_sort():
    time = [c for c in cost] # 시간 후보 넣는 리스트
    q = deque()

    # 첫시작 : 선수과목 (indegree) 가 0인 노드 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        # result.append(now)
        # 현재 노드 소요시간 갱신
        # cost[now] += max(time[now])
        # 연결 노드 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 연결 노드의 시간 리스트에 추가
            # time[i].append(cost[now])
            time[i] = max(time[i], cost[i]+time[now])
            # 새롭게 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for t in time[1:]:
        print(t)

topology_sort()




    

               

