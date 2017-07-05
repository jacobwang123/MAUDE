import os
import numpy as np
import pandas as pd
from fuzzywuzzy import fuzz

cwd = os.path.dirname(os.path.realpath(__file__))

def fuzzy_match(line):
	b = False
	if 'ALCL' in line:
		b = True
	if (fuzz.partial_ratio('anaplastic large cell lymphoma', line) >= 90):
		b = True
	return b

if __name__ == '__main__':
	df = pd.read_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=0, encoding='ISO-8859-1')
	df['ALCL'] = np.nan
	df['ALCL'] = df['FOI_TEXT'].map(fuzzy_match)
	print(df.loc[df['ALCL']==True, :].shape[0])