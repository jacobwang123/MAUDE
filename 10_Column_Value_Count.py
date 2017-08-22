import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))


# df_FOI = pd.read_csv('D:/Workplace/MAUDE/Data/MDRFOI_BI_FULL_TABLE.txt', sep='|', header=0, encoding='ISO-8859-1',
#                      error_bad_lines=False)
# a = df_FOI['SOURCE_TYPE'].value_counts()
# a.to_csv('mdrfoi_SOURCE_TYPE_full_list.csv')

df_FOI = pd.read_csv('D:/Workplace/MAUDE/WF/DEV_BI_FULL_TABLE.txt', sep='|', header=0, encoding='ISO-8859-1',
                     error_bad_lines=False)
a.to_csv('D:/Workplace/MAUDE/FDA_0824_Weekly_Report/foidev_brand_name_full_list.csv')