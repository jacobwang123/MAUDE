# with open('NEW_ALCL(anaplastic).txt', 'r', encoding='utf8') as rf:
# 	with open('ALCL_anaplastic.txt', 'w', encoding='utf8') as wf:
# 		for line in rf:
# 			line = line.split('|')
# 			a = line[0]
# 			wf.write(a)
# 			wf.write('\n')

import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))

MDR_FOI_LIST = ['', 'Add', 'Change', 'Thru2016']
for s in MDR_FOI_LIST:
	mdr = pd.read_csv(os.path.join(cwd, 'foidev', 'mdrfoi'+s+'.txt'), sep='|', header=0, encoding='ISO-8859-1',
	                 error_bad_lines=False)
print(mdr.shape[0])
l = []
with open('1_Total_BI_Report_Number_List.txt', 'r') as rf:
	for line in rf:
		line = line.replace('\n', '')
		l.append(line)
	rf.close()
m = mdr.loc[mdr['REPORT_NUMBER'].isin(l)]
print(m.shape[0])
m.to_csv('MDRFOI_BI_FULL_TABLE.txt', index=False, sep='|')