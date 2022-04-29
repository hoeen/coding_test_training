from collections import deque

t = int(input())

ans_list = []

for _ in range(t):
    n = int(input())
    hx, hy = map(int, input().split())
    conv_list = []
    for _ in range(n):
        conv_list.append(list(map(int, input().split())))
    px, py = map(int, input().split())
    visited = []

    def dfs():
        st = deque([(hx,hy)])
        while st:
            nx, ny = st.pop()
            visited.append((nx,ny))
            if abs(nx-px) + abs(ny-py) <= 1000:
                return True
            else:
                for cx, cy in conv_list:
                    if abs(nx-cx) + abs(ny-cy) <= 1000 and (cx,cy) not in visited:
                        st.append((cx,cy))
        return False
    if dfs():
        ans_list.append('happy')
    else:   
        ans_list.append('sad')


# n, home, conv_list, px, py

for ans in ans_list:
    print(ans)



    
                    
                
                
                
                
                
                



        
    


