import os
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz
from multiprocessing import Pool, cpu_count

thread_num = cpu_count()
cwd = os.path.dirname(os.path.realpath(__file__))

def fuzzy_match(line):
	b = False
	if 'ALCL' in line:
		b = True
	if (fuzz.partial_ratio('anaplastic large cell lymphoma', line) >= 90):
		b = True
	return b

def assign(thread):
	if thread == thread_num - 1:
		temp_list = FOI_TEXT_LIST[thread * trunk:]
	else:
		temp_list = FOI_TEXT_LIST[thread * trunk : (thread+1) * trunk]

	for s in temp_list:
		df = pd.read_csv(os.path.join(cwd, 'foitext_normalized', 'foitext_normalized'+s+'.txt'), sep='|', header=0,
					     encoding='ISO-8859-1', error_bad_lines=False)
		df['ALCL'] = np.nan
		df['FOI_TEXT'] = df['FOI_TEXT'].astype(str)
		df['ALCL'] = df['FOI_TEXT'].map(fuzzy_match)
		df = df.loc[df['ALCL']==True, ['MDR_REPORT_KEY', 'FOI_TEXT']]
		if s == '':
			df['LABEL'] = 'new'
		else:
			df['LABEL'] = s
		df.to_csv(os.path.join(cwd, 'ALCL.txt'), sep='|', header=True, index=False, mode='a')

if __name__ == '__main__':
	# df = pd.read_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=0, encoding='ISO-8859-1')
	# df['ALCL'] = np.nan
	# df['ALCL'] = df['FOI_TEXT'].map(fuzzy_match)
	# print(df.loc[df['ALCL']==True, :].shape[0])

	FOI_TEXT_LIST = ['', 'Add', 'Change', 'thru1995']
	for i in range(1996, 2017):
		FOI_TEXT_LIST.append(str(i))

	trunk = int(len(FOI_TEXT_LIST)/thread_num) + 1
	p = Pool(thread_num)
	p.map(assign, range(thread_num))
