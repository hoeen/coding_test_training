# 20분 소요
# survey = ["AN", "CF", "MJ", "RT", "NA"]
# choices = [5,3,2,7,5]

survey = ["TR", "RT", "TR"]
choices = [7,1,3]
'''
dict 로 8가지 지표마다 점수 부여 
1234567
각 survey마다 문자 나눠서, if로 점수 부여
모든 survey 끝나면, RT, CF, JM, AN묶어서 높은것을 내놓기. 같으면 앞것.
'''
per_dict = {
    'R':0,
    'T':0,
    'C':0,
    'F':0,
    'J':0,
    'M':0,
    'A':0,
    'N':0
}
key = list(per_dict.keys())
# print(key)
for i in range(len(survey)):
    front, back = survey[i][0], survey[i][1]
    score = choices[i]
    if score < 4:
        per_dict[front] += 4-score
    elif score > 4:
        per_dict[back] += score-4

answer = ''
for i in range(0,8,2):
    comp = []
    for j in range(2):
        comp.append(key[i+j])
    if per_dict[comp[0]] >= per_dict[comp[1]]:
        answer += comp[0]
    else:
        answer += comp[1]
    
print(answer)
        



# result = 'TCMA'