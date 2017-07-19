import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))

MDR_FOI_LIST = ['', 'Add', 'Change', 'Thru2016']
for s in MDR_FOI_LIST:
	mdr = pd.read_csv(os.path.join(cwd, 'foidev', 'mdrfoi'+s+'.txt'), sep='|', header=0, encoding='ISO-8859-1',
	                 error_bad_lines=False)
print(mdr.shape[0])

key = pd.read_csv(os.path.join(cwd, 'FDA_File', '3_Final_BI_KEY_List.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
print(key.shape[0])

alcl = pd.read_csv(os.path.join(cwd, 'FDA_File', '5_ALCL.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
print(alcl.shape[0])

alcl_bi = pd.read_csv(os.path.join(cwd, 'FDA_File', '5_BI_ALCL_KEY_list.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
print(alcl_bi.shape[0])

key_result = pd.merge(key, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
print(key_result.shape[0])
key_result = key_result['REPORT_NUMBER']
key_result.to_csv('D:/Workplace/MAUDE/key_result.txt')

alcl_result = pd.merge(alcl, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
print(alcl_result.shape[0])
alcl_result = alcl_result['REPORT_NUMBER']
alcl_result.to_csv('D:/Workplace/MAUDE/alcl_result.txt')

alcl_bi_result = pd.merge(alcl_bi, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
print(alcl_bi_result.shape[0])
alcl_bi_result = alcl_bi_result['REPORT_NUMBER']
alcl_bi_result.to_csv('D:/Workplace/MAUDE/alcl_bi_result.txt')


#String manipulation
with open('alcl_bi_result.txt', 'r', encoding='utf-8') as r:
	with open('3_ALCL_BI_Number_List.txt', 'w', encoding='utf-8') as w:
		for line in r:
			line = line.split(',')
			w.write(line[1])
