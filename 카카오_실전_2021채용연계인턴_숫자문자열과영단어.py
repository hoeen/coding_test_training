# ~ 7:20
import re
eng_list = ['zero', 'one', 'two', 'three', 'four', 'five',
            'six', 'seven', 'eight', 'nine']
for i in range(len(eng_list)):
    answer = re.sub(eng_list[i],str(i),s)