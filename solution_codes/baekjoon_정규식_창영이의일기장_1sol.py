import re

text = input()
pat = 'aeiou'
for i in range(5):
    text = re.sub(pat[i]+'p'+pat[i],pat[i],text)
print(text)