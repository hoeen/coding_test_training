#3:30
def solution(record):
    result = {}
    for r in record:
        if len(r.split()) == 2:
            com, userid = r.split()
        elif len(r.split()) == 3:
            com, userid, name = r.split()
        # print(r.split())
        if com != 'Leave':
            result[userid] = name
    
    answer = []
    for r in record:
        if len(r.split()) == 2:
            com, userid = r.split()
        elif len(r.split()) == 3:
            com, userid, name = r.split()
        if com == 'Enter':
            answer.append(f'{result[userid]}님이 들어왔습니다.')
        elif com == 'Leave':
            answer.append(f'{result[userid]}님이 나갔습니다.')
        
    return answer