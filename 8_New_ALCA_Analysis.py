import os
import numpy as np
import pandas as pd
cwd = os.path.dirname(os.path.realpath(__file__))

aa = pd.read_csv(os.path.join(cwd, 'aaa_result.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
al = pd.read_csv(os.path.join(cwd, 'ala_result.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
frames = [aa, al]
result = pd.concat(frames)

print(result.shape[0])

a = result.drop_duplicates()


print(a.shape[0])
a.to_csv('D:/Workplace/MAUDE/a.txt', index=False)

bi = pd.read_csv(os.path.join(cwd, '1_Total_BI_Report_Number_List.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)

a_result = pd.merge(a, bi, how='inner', on='REPORT_NUMBER', left_index = True, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False)
print(a_result.shape[0])

a_result.to_csv('D:/Workplace/MAUDE/a_BI.txt', index=False)

alcl = pd.read_csv(os.path.join(cwd, '5_ALCL_Report_Number_List.txt'), sep='|', header=0,
                  encoding='ISO-8859-1', error_bad_lines=False)
frames = [a_result, alcl]
result = pd.concat(frames)
print(result.shape[0])

a = result.drop_duplicates()


print(a.shape[0])

