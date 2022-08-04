# 풀이 시간 45분
from collections import deque

def solution(rows, columns, queries):
    
    board = []
    for i in range(rows):
        board.append([i*columns+a for a in range(1, columns+1)])
    
    answer = []
    # 마지막 쿼리는 돌릴 필요 없음.
    for i in range(len(queries)):
        
        # 테두리 뽑아서 큐에 저장
        x1, y1, x2, y2 = queries[i]
        x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
        q = deque([])
        # 윗변
        for j in range(y1, y2):
            q.append(board[x1][j])
        # 오른쪽
        for j in range(x1, x2):
            q.append(board[j][y2])
        # 아랫변
        for j in range(y2, y1, -1):
            q.append(board[x2][j])
        # 왼쪽
        for j in range(x2, x1, -1):
            q.append(board[j][y1])
        
        answer.append(min(q))
        
        if i < len(queries)-1:
            ### 큐 하나 밀려서 뽑아서 배열 넣기
            for j in range(y1, y2):
                num = q.popleft()
                board[x1][j+1] = num
            # 오른쪽
            for j in range(x1, x2):
                num = q.popleft()
                board[j+1][y2] = num
            # 아랫변
            for j in range(y2, y1, -1):
                num = q.popleft()
                board[x2][j-1] = num
            # 왼쪽
            for j in range(x2, x1, -1):
                num = q.popleft()
                board[j-1][y1] = num
        
    return answer