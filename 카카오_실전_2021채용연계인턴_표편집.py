# ~10:30
# 추가,삭제가 빈번하므로 연결 리스트를 이용해서 풀어야 효율성 테스트 통과 가능
class Node():
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None    

def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]

    curr = nodeArr[k]
    mystack = []

    for str in cmd:
        if str[0] == 'U':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.prev
        elif str[0] == 'D':
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == 'C':
            mystack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = mystack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += 'X'
        else:
            answer += 'O'
    return answer

cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(8,2,cmd))


### 시도했던 내 풀이 - 리스트를 활용했기 때문에 효율성 테스트 통과 못함
# n, k = 8, 2 # 표의 행 개수, 처음 위치 
# now = k
# cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z", "U 1", "C"]
# init = [i for i in range(n)]
# start = [i for i in range(n)]
# # init = [False]*n
# q = deque([]) # 삭제순으로 넣어짐
# # ux, dx, c, z

# def binary_insert(array, target, start, end): # 리스트, 찾는숫자
#     if start > end:
#         return False
#     elif start == end: # 하나 남은경우 - 비교하여 옆에 붙임
#         if array[start] < target:
#             array.insert(start+1,target)
#         else:
#             array.insert(start,target)
#         return array
#     mid = (start + end)//2
#     # 각 위치마다 양옆을 비교하여 작고 큰지 확인한다.
#     if array[mid] < target < array[mid+1]:
#         array.insert(mid+1,target)
#         return array
#     elif array[mid] < target:
#         return binary_insert(array,target,mid+1,end)
#     elif array[mid] > target:
#         return binary_insert(array,target,start,mid-1)



# for c in cmd:
#     print(c)
#     # D , U
#     if c[0] == 'D':
#         num = int(c[2])
#         now += num 
#     elif c[0] == 'U':
#         num = int(c[2])
#         now -= num
#     elif c[0] == 'C': # 삭제 - 현재위치의 갱신 필요
#         dn = init.pop(now)
#         q.append(dn)
#         if now == len(init): # 마지막칸일경우
#             now -= 1
#     else: #z
#         ret = q.pop() # 최근삭제된것이 빠짐
#         # now 와 ret 의 비교? 
#         if init[now] > ret: # 복귀된것이 더 앞숫자
#             now += 1 # 순서가 밀리므로 하나 더함
#         init = binary_insert(init, ret, 0, len(init)-1)
        
#     print('now', now)
#     print(init)
#     print(q)
# dif = set(start) - set(init)
# answer = ['O']*n
# for d in dif:
#     answer[d] = 'X'
# answer = ''.join(answer)
# print(answer)


