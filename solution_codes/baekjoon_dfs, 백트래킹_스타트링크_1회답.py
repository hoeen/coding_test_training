# ~1:00 ~ 1:15
# from collections import deque

f, s, g, u, d = map(int, input().split())
# f층, 목적지 g층, 현재 s층, u층 위로 이동, d층 아래로 이동. 

# f, s, g, u, d = 10, 1, 10, 2, 1
visited = [int(1e9)]*(f+1)
min_press = int(1e9)
# up, down 을 눌러보며 찾는다. bfs?
def dfs(level, press):
    global min_press, visited
    # breakpoint()
    
    print(f'level: {level}, pressed: {press}')
    print(visited)

    if level < 1 or level > f:
        return   

    if visited[level] <= press: # 이미 도달한적 있음
        return
    else:
        visited[level] = press # 갱신
        if level == g:
            min_press = press
            return
        if u > 0:
            print(f'up: {level} to {level+u}')
            dfs(level+u, press+1)
        
        if d > 0:
            print(f'down: {level} to {level-d}')
            dfs(level-d, press+1)
    
    
dfs(s, 0)
if min_press != int(1e9):
    print(min_press)
else:
    print('use the stairs')


