def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(a, b, parent):
    
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, costs):
    answer = 0
    parent = list(range(0, n))
    
    costs.sort(key=lambda x: x[2]) #맨 뒤 cost가 짧은것부터 정렬
    
    for a, b, cost in costs:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(a, b, parent)
            answer += cost

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))



n행 m열의 격자가 있습니다. 격자의 각 행은 0, 1, ..., n-1번의 번호, 그리고 각 열은 0, 1, ..., m-1번의 번호가 순서대로 매겨져 있습니다. 당신은 이 격자에 공을 하나 두고, 그 공에 다음과 같은 쿼리들을 날리고자 합니다.
열 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(0, dx))
열 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(1, dx))
행 번호가 감소하는 방향으로 dx칸 이동하는 쿼리 (query(2, dx))
행 번호가 증가하는 방향으로 dx칸 이동하는 쿼리 (query(3, dx))
단, 공은 격자 바깥으로 이동할 수 없으며, 목적지가 격자 바깥인 경우 공은 이동하다가 더 이상 이동할 수 없을 때 멈추게 됩니다. 예를 들어, 5행 × 4열 크기의 격자 내의 공이 3행 2열에 있을 때 query(3, 10) 쿼리를 받은 경우 공은 4행 2열에서 멈추게 됩니다. (격자의 크기가 5행 × 4열이므로, 0~4번 행과 0~3번 열로 격자가 구성되기 때문입니다.)
격자의 행의 개수 n, 열의 개수 m, 정수 x와 y, 그리고 쿼리들의 목록을 나타내는 2차원 정수 배열 queries가 매개변수로 주어집니다. n × m개의 가능한 시작점에 대해서 해당 시작점에 공을 두고 queries 내의 쿼리들을 순서대로 시뮬레이션했을 때, x행 y열에 도착하는 시작점의 개수를 return 하도록 solution 함수를 완성해주세요.
제한사항
1 ≤ n ≤ 109
1 ≤ m ≤ 109
0 ≤ x < n
0 ≤ y < m
1 ≤ queries의 행의 개수 ≤ 200,000
queries의 각 행은 [command,dx] 두 정수로 이루어져 있습니다.
0 ≤ command ≤ 3
1 ≤ dx ≤ 109
이는 query(command, dx)를 의미합니다.
입출력 예
n	m	x	y	queries	result
2	2	0	0	[[2,1],[0,1],[1,1],[0,1],[2,1]]	4
2	5	0	1	[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]	2
입출력 예 설명
입출력 예 #1
다음 애니메이션은 4개의 가능한 시작점에 대한 모든 시뮬레이션을 나타낸 것입니다.
ex1
어떤 곳에서 출발하더라도 항상 0행 0열에 도착하기 때문에, 4를 return 해야 합니다.
입출력 예 #2
다음 애니메이션은 10개의 가능한 시작점에 대한 모든 시뮬레이션을 나타낸 것입니다.