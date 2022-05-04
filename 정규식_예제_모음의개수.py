import re
# text = '''How are you today?
# Quite well, thank you, how about yourself?
# I live at number twenty four.
# '''

while True:
    text = input()
    if text == '#':
        break
    vow_list = re.findall('[aeiou]', text)
    print(len(vow_list))
    