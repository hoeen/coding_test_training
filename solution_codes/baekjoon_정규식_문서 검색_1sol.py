import re
text = input()
word = input()
# 처음부터 매치시켜서 없애 나간다. greedy
print(len(re.findall(word,text)))