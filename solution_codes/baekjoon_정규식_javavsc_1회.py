# 밑줄 있으면 c, 대문자 있으면 java
# java - 첫단어 소문자, 다음단어부터는 첫글자만 대문자. -대문자로 단어 파악
# c - _로 단어 파악
import re
text = input()
# 탈락조건 : 첫번째 대문자.  밑줄과 대문자가 같이 있는 경우.
# 탈락조건 통과 - java - 대문자를 소문자로 바꾸고 _소문자 로 치환.
# c - _소문자 를 대문자로 치환.
def answer():
    # global newtext
    if text[0] == '_' or text[-1] == '_' or \
        re.search('_{2,}',text) or text[0].isupper() or \
            (re.search('_',text) and re.search('[A-Z]',text)):
        print('Error!')
        return
    elif re.search('_',text):
        # _소문자 -> 대문자
        newtext = re.sub('_[a-z]', lambda x: x.group(1).upper(),text)
    elif re.search('[A-Z]',text):
        # 대문자 -> _소문자
        newtext = re.sub('[A-Z]', lambda x: '_'+x.group(0).lower(), text)
    else:
        newtext = text
    print(newtext)
    return

answer()


    
