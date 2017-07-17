import pandas as pd
import os
import numpy as np

cwd = os.path.dirname(os.path.realpath(__file__))
FOI_DEV_LIST = [] # '', 'Add', 'Change'
for i in range(1998, 2008):
	FOI_DEV_LIST.append(str(i))

df_BI = pd.read_csv(os.path.join(cwd, '1_BI_KEY_list.txt'), header=None, names=['MDR_REPORT_KEY'])
df_list = []
for s in FOI_DEV_LIST:
	df = pd.read_csv(os.path.join(cwd, 'foidev', 'foidev'+s+'.txt'), sep='', '', header=0,
					    		  encoding='ISO-8859-1', error_bad_lines=False)
	df_list.append(df)
df_BASELINE = pd.concat(df_list, axis=0)
del df_list

df_BI_BASELINE = pd.merge((df_BASELINE, df_BI), on=['MDR_REPORT_KEY'], how='inner')

baseline_col = ['BASELINE_BRAND_NAME', 'BASELINE_GENERIC_NAME', 'BASELINE_MODEL_NO', 'BASELINE_CATALOG_NO',
				'BASELINE_OTHER_ID_NO', 'BASELINE_DEVICE_FAMILY', 'BASELINE_SHELF_LIFE_CONTAINED',
				'BASELINE_SHELF_LIFE_IN_MONTHS', 'BASELINE_PMA_FLAG', 'BASELINE_PMA_NO', 'BASELINE_510_K__FLAG',
				'BASELINE_510_K__NO', 'BASELINE_PREAMENDMENT', 'BASELINE_TRANSITIONAL', 'BASELINE_510_K__EXEMPT_FLAG',
				'BASELINE_DATE_FIRST_MARKETED', 'BASELINE_DATE_CEASED_MARKETING']
for b in baseline_col:
	print(b, 'missing :' df_BI_BASELINE.loc[df_BI_BASELINE[b]==np.nan, :].shape[0])
