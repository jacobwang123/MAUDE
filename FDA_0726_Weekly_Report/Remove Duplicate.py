l = []
with open('2_ALCL_Number_List.txt', 'r', encoding='utf8') as rf:
	with open('5_ALCL_Number_List.txt', 'w', encoding='utf8') as wf:
		for line in rf:
			a = line.replace('\n', '')
			if a not in l:
				l.append(a)
				wf.write(line)