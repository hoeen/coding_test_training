import re

order = []
exists = False
for i in range(5):
    text = input()
    if re.search('FBI', text) != None:
        order.append(str(i+1))
        exists = True
if not exists:
    print('HE GOT AWAY!')
else:
    print(' '.join(order))


    import re
print(re.sub(r'([aeiou])p\1', r'\1', input()))