'''
https://velog.io/@heyksw/Python-백준-platinum-23291-어항-정리'''

from collections import deque
import sys
N, K = (8, 7)#map(int, sys.stdin.readline().split())
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = deque([5,2,3,14,9,2,11,8])
# board = list()
# board.append(deque(list(map(int, sys.stdin.readline().split()))))

# 물고기가 가장 적은 어항에 물고기 한 마리 넣기
def push_fish_to_min_bowl(graph):
    min_bowl_fish_num = min(graph[0])
    for i in range(len(graph[0])):
        if graph[0][i] == min_bowl_fish_num:
            graph[0][i] += 1

# 가장 왼쪽의 어항을 위에 쌓기
def popleft_and_stack(graph):
    pop = graph[0].popleft()
    graph.append(deque([pop]))

print(board)
push_fish_to_min_bowl(board)
popleft_and_stack(board)
print(board)