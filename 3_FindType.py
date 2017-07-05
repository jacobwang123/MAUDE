import os
import pickle
import numpy as np
import pandas as pd

cwd = os.path.dirname(os.path.realpath(__file__))

def process_fill():
	FOI_DEV_LIST = ['', 'Add', 'Change']
	for i in range(1998, 2017):
		FOI_DEV_LIST.append(str(i))

	total_FWM = {}
	total_FTR = {}
	FWM_num = 0
	FTR_num = 0
	for s in FOI_DEV_LIST:
		df = pd.read_csv(os.path.join(cwd, 'foidev', 'foidev'+s+'.txt'), sep='|', header=0,
					     encoding='ISO-8859-1', error_bad_lines=False)
		FWM = list(df.loc[df['DEVICE_REPORT_PRODUCT_CODE']=='FWM', 'MDR_REPORT_KEY'])
		FTR = list(df.loc[df['DEVICE_REPORT_PRODUCT_CODE']=='FTR', 'MDR_REPORT_KEY'])

		FWM = list(set(FWM))
		FTR = list(set(FTR))
		FWM_num += len(FWM)
		FTR_num += len(FTR)

		if s == '':
			total_FWM.update({'new':FWM})
			total_FTR.update({'new':FTR})
		else:
			total_FWM.update({s:FWM})
			total_FTR.update({s:FTR})

	with open(os.path.join(cwd, 'FWM_list.txt'), 'ab+') as f1:
		pickle.dump(total_FWM, f1)
	with open(os.path.join(cwd, 'FTR_list.txt'), 'ab+') as f2:
		pickle.dump(total_FTR, f2)

	return (FWM_num, FTR_num)

def match_surface(s):
	if 'smooth' in str(s):
		return 's'
	elif 'textured' in str(s):
		return 't'
	else:
		return np.nan

def process_surface():
	FOI_DEV_LIST = ['', 'Add', 'Change']
	for i in range(1998, 2017):
		FOI_DEV_LIST.append(str(i))
	FOI_TEXT_LIST = ['', 'Add', 'Change', 'thru1995']
	for i in range(1996, 2017):
		FOI_TEXT_LIST.append(str(i))

	total_smooth = {}
	total_textured = {}
	smooth_num = 0
	textured_num = 0

	df = pd.read_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=0, encoding='ISO-8859-1')
	df['filter'] = df['FOI_TEXT'].map(match_surface)
	temp = df.loc[df['filter']=='s', :]
	temp = pd.DataFrame(temp.groupby(['LABEL'])['MDR_REPORT_KEY'].apply(list))
	for index, value in temp.iterrows():
		total_smooth.update({str(index):value['MDR_REPORT_KEY']})
		smooth_num += len(value['MDR_REPORT_KEY'])
	# ts = list(df['MDR_REPORT_KEY'])
	temp = df.loc[df['filter']=='t', :]
	temp = pd.DataFrame(temp.groupby(['LABEL'])['MDR_REPORT_KEY'].apply(list))
	for index, value in temp.iterrows():
		total_textured.update({str(index):value['MDR_REPORT_KEY']})

	for s in FOI_DEV_LIST:
		tt = []
		f = open(os.path.join(cwd, 'foidev', 'foidev'+s+'.txt'), encoding='ISO-8859-1')
		lines = f.readlines()[1:]
		f.close()
		for line in lines:
			if ('BIOCELL' in line) or ('SILEX' in line) or ('MISTI' in line) or ('\bSCL\b' in line) or ('AVANTEX' in line) or ('SURGITEK' in line) or ('MENTOR Memory Shape' in line):
				key = int(line.split('|')[0])
				tt.append(key)
		if s == '':
			s = 'new'

		try:
			original_t = total_textured[s]
			tt = list(set(tt + original_t))
		except:
			tt = list(set(tt))
		textured_num += len(tt)
		total_textured.update({s:tt})
	# tt = list(df['MDR_REPORT_KEY'])

	# ts = list(set(ts))
	# try:
	# 	original_t = total_textured[s]
	# 	tt = list(set(tt + original_t))
	# except:
	# 	tt = list(set(tt))
	# smooth_num += len(ts)
	# textured_num += len(tt)
	# total_smooth.update({s:ts})
	# total_textured.update({s:tt})

	with open(os.path.join(cwd, 'smooth_list.txt'), 'ab+') as f1:
		pickle.dump(total_smooth, f1)
	with open(os.path.join(cwd, 'textured_list.txt'), 'ab+') as f2:
		pickle.dump(total_textured, f2)

	return (smooth_num, textured_num)

if __name__ == '__main__':
	# print(process_fill())
	print(process_surface())

	# with open(os.path.join(cwd, 'smooth_list.txt'), 'rb') as f1:
	# 	total_smooth = pickle.load(f1)
	# with open(os.path.join(cwd, 'textured_list.txt'), 'rb') as f2:
	# 	total_textured = pickle.load(f2)
