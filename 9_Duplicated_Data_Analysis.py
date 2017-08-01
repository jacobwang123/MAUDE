import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))

# l = []
# d = []
# n = 0
# with open('foitext2016.txt', 'r') as rf:
# 	for line in rf:
# 		try:
# 			line = line.replace('\n', '')
# 			if line not in l:
# 				l.append(line)
# 			elif line not in d:
# 				d.append(line)
# 			n = n + 1
# 			print(n, len(l), len(d))
# 		except:
# 			continue

a = pd.read_csv('D:/Workplace/MAUDE/foidev/foitext2015.txt', sep='|', header=0, encoding='ISO-8859-1',
                error_bad_lines=False)
k = a['MDR_REPORT_KEY']
print(k.shape[0])
k.to_csv('D:/Workplace/MAUDE/foitext2016.txt', index=False)
kd = k.drop_duplicates()
print(kd.shape[0])