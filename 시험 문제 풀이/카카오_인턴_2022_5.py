rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]

from collections import deque

shift_dic = {}
rotate_dic ={}
def shiftrow(rc):
    if tuple([tuple(k) for k in rc]) in shift_dic.keys():
        return shift_dic[rc]
    else:
        new_rc = []
        q = deque(rc)
        new_rc.append(q.pop())
        for _ in range(len(q)):
            new_rc.append(q.popleft())
            
        shift_dic[tuple([tuple(k) for k in rc])] = new_rc
        print(shift_dic)
        return new_rc
    
def rotate(rc):
    if tuple([tuple(k) for k in rc]) in rotate_dic.keys():
        return rotate_dic[rc]
    else:
        q = deque([])
        ylen = len(rc[0])
        xlen = len(rc)
        for y in range(ylen-1):
            q.append(rc[0][y])
        for x in range(xlen-1):
            q.append(rc[x][ylen-1])
        for y in range(ylen-1, 0, -1):
            q.append(rc[xlen-1][y])
        for x in range(xlen-1, 0, -1):
            q.append(rc[x][0])

        # 다시 집어넣기
        rot_rc = [r[:] for r in rc]
        for y in range(1,ylen):
            rot_rc[0][y] = q.popleft()
        for x in range(1,xlen):
            rot_rc[x][ylen-1] = q.popleft()
        for y in range(ylen-2, -1, -1):
            rot_rc[xlen-1][y] = q.popleft()
        for x in range(xlen-2, -1, -1):
            rot_rc[x][0] = q.popleft()
        rotate_dic[tuple([tuple(k) for k in rot_rc])] = rot_rc
        return rot_rc
    # 줄로 뽑기

for op in operations:
    if op == 'Rotate':
        rc = rotate(rc)
        for n in rc:
            print(n)
    else:
        rc = shiftrow(rc)
        for n in rc:
            print(n)



for n in rc:
    print(n)


# result = [[8, 9, 6], [4, 1, 2], [7, 5, 3]]