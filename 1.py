with open('alcl_bi_result.txt', 'r', encoding='utf-8') as r:
	with open('3_ALCL_BI_Number_List.txt', 'w', encoding='utf-8') as w:
		for line in r:
			line = line.split(',')
			w.write(line[1])
