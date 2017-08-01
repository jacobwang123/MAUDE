import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))

# MDR_FOI_LIST = ['', 'Add', 'Change', 'Thru2016']
# for s in MDR_FOI_LIST:
# 	mdr = pd.read_csv(os.path.join(cwd, 'foidev', 'mdrfoi'+s+'.txt'), sep='|', header=0, encoding='ISO-8859-1',
# 	                 error_bad_lines=False)
# print(mdr.shape[0])

# key = pd.read_csv(os.path.join(cwd, 'FDA_File', '3_Final_BI_KEY_List.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(key.shape[0])
#
# alcl = pd.read_csv(os.path.join(cwd, 'FDA_File', '5_ALCL.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(alcl.shape[0])
#
# alcl_bi = pd.read_csv(os.path.join(cwd, 'FDA_File', '5_BI_ALCL_KEY_list.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(alcl_bi.shape[0])
#
# key_result = pd.merge(key, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(key_result.shape[0])
# key_result = key_result['REPORT_NUMBER']
# key_result.to_csv('D:/Workplace/MAUDE/key_result.txt')
#
# alcl_result = pd.merge(alcl, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(alcl_result.shape[0])
# alcl_result = alcl_result['REPORT_NUMBER']
# alcl_result.to_csv('D:/Workplace/MAUDE/alcl_result.txt')
#
# alcl_bi_result = pd.merge(alcl_bi, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(alcl_bi_result.shape[0])
# alcl_bi_result = alcl_bi_result['REPORT_NUMBER']
# alcl_bi_result.to_csv('D:/Workplace/MAUDE/alcl_bi_result.txt')

# text = pd.read_csv(os.path.join(cwd, 'FDA_File', '1_Text_BI_List.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(text.shape[0])
#
# text_result = pd.merge(text, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(text_result.shape[0])
# text_result = text_result['REPORT_NUMBER']
# text_result.to_csv('D:/Workplace/MAUDE/text_result.txt')

# FTR = pd.read_csv(os.path.join(cwd, 'FDA_File', '2_FTR_List.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(FTR.shape[0])
#
# FTR_result = pd.merge(FTR, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(FTR_result.shape[0])
# FTR_result = FTR_result['REPORT_NUMBER']
# FTR_result.to_csv('D:/Workplace/MAUDE/FTR_result.txt')

# FWM = pd.read_csv(os.path.join(cwd, 'FDA_File', '2_FWM_List.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(FWM.shape[0])
#
# FWM_result = pd.merge(FWM, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(FWM_result.shape[0])
# FWM_result = FWM_result['REPORT_NUMBER']
# FWM_result.to_csv('D:/Workplace/MAUDE/FWM_result.txt')
#
# #String manipulation
# with open('FWM_result.txt', 'r', encoding='utf-8') as r:
# 	with open('3_FWM_result.txt.txt', 'w', encoding='utf-8') as w:
# 		for line in r:
# 			line = line.split(',')
# 			w.write(line[1])

# aa = pd.read_csv(os.path.join(cwd, 'ALCL_anaplastic.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(aa.shape[0])
#
# aa_result = pd.merge(aa, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(aa_result.shape[0])
# aa_result = aa_result['REPORT_NUMBER']
# aa_result.to_csv('D:/Workplace/MAUDE/aa_result.txt')
#
# al = pd.read_csv(os.path.join(cwd, 'ALCL_lymphoma.txt'), sep='|', header=0,
#                   encoding='ISO-8859-1', error_bad_lines=False)
# print(al.shape[0])
#
# al_result = pd.merge(al, mdr, how='inner', on='MDR_REPORT_KEY', left_index = True, right_index=False, sort=True,
#          suffixes=('_x', '_y'), copy=True, indicator=False)
# print(al_result.shape[0])
# al_result = al_result['REPORT_NUMBER']
# al_result.to_csv('D:/Workplace/MAUDE/al_result.txt')

with open('al_result.txt', 'r', encoding='utf-8') as r:
	with open('ala_result.txt', 'w', encoding='utf-8') as w:
		for line in r:
			line = line.split(',')
			w.write(line[1])