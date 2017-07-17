import os
import pickle
import pandas as pd

cwd = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(cwd, 'FWM_list.txt'), 'rb') as f1:
	FWM_dict = pickle.load(f1)
with open(os.path.join(cwd, 'FTR_list.txt'), 'rb') as f2:
	FTR_dict = pickle.load(f2)

FWM_list = []
for key in FWM_dict:
	for i in FWM_dict[key]:
		FWM_list.append(i)

FTR_list = []
for key in FTR_dict:
	for i in FTR_dict[key]:
		FTR_list.append(i)

FILL_list = FWM_list + FTR_list

df = pd.read_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=0, encoding='ISO-8859-1', error_bad_lines=False)
MY_list = list(df.MDR_REPORT_KEY.unique())

inter = list(set(FILL_list) & set(MY_list))
union = list(set(FILL_list + MY_list))

print(len(union))
with open(os.path.join(cwd, 'BI_KEY_list.txt'), 'w') as f:
	for i in union:
		f.write(str(i) + '\n')



df = pd.read_csv(os.path.join(cwd, 'ALCL.txt'), sep='|', header=0, encoding='ISO-8859-1', error_bad_lines=False)
ALCL = list(df.MDR_REPORT_KEY.unique())

inter = list(set(union) & set(ALCL))
print(len(inter))
with open(os.path.join(cwd, 'BI_ALCL_KEY_list.txt'), 'w') as f:
	for i in inter:
		f.write(str(i) + '\n')