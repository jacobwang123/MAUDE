import os
import pandas as pd
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from fuzzywuzzy import fuzz
from multiprocessing import Pool, cpu_count

thread_num = cpu_count()
KEYWORD_LIST_FIRST = ['breast pain', 'breast swelling', 'breast cyst', 'breast calcification', 'capsular contracture',
					  'lymph node enlargement', 'firmness of breast', 'breast implant', 'breast augmentation',
					  'breast enlargement', 'mammary implant', 'mammary augmentation', 'mammary enlargement',
					  'mammary swelling', 'breate prosthesis', 'mammary prosthesis']

KEYWORD_LIST_SECOND = ['hematoma', 'mass', 'lump', 'rupture', 'deflated', 'infection', 'abscess', 'leukopenia',
					   'nodules', 'skin discoloration', 'skin lesion', 'seroma', 'effusion', 'fluid']

cwd = os.path.dirname(os.path.realpath(__file__))
lmtzr = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
stopwords = nltk.corpus.stopwords.words('english')

def processLine(line):
    line = line.lower()
    tokens = tokenizer.tokenize(line)
    output = []
    for t in tokens:
        t = lmtzr.lemmatize(t)
        if (len(t) <= 2) or (len(t) >= 15) or (t in stopwords) or (t.isdigit()):
            continue
        output.append(t)
    return ' '.join(output)

def fuzzy_match(line):
	b = False
	for k in KEYWORD_LIST_FIRST:
		if fuzz.partial_ratio(k, line) >= 95:
			b = True
			break
		if (fuzz.partial_ratio(k, line) >= 95) & (('breast' in line) | ('mammary' in line)) & (len(line) >= 5):
			b = True
			break
	return b

def assign(thread):
	if thread == thread_num - 1:
		temp_list = FOI_TEXT_LIST[thread * trunk:]
	else:
		temp_list = FOI_TEXT_LIST[thread * trunk : (thread+1) * trunk]

	for s in temp_list:
		# df = pd.read_csv(os.path.join(cwd, 'foitext', 'foitext'+s+'.txt'), sep='|', header=0,
		# 			     encoding='ISO-8859-1', error_bad_lines=False)
		# df['FOI_TEXT'] = df['FOI_TEXT'].astype(str)
		# df['FOI_TEXT'] = df['FOI_TEXT'].map(processLine)
		# df.to_csv(os.path.join(cwd, 'foitext_normalized', 'foitext_normalized'+s+'.txt'), sep='|', header=True, index=False)
		df = pd.read_csv(os.path.join(cwd, 'foitext_normalized', 'foitext_normalized'+s+'.txt'), sep='|', header=0,
					     encoding='ISO-8859-1', error_bad_lines=False)
		df['FOI_TEXT'] = df['FOI_TEXT'].astype(str)
		df['filter'] = df['FOI_TEXT'].map(fuzzy_match)
		df = df.loc[df['filter']==True, ['MDR_REPORT_KEY', 'FOI_TEXT']]
		if s == '':
			df['LABEL'] = 'new'
		else:
			df['LABEL'] = s
		df.to_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=False, index=False, mode='a')

if __name__ == '__main__':
	FOI_TEXT_LIST = ['', 'Add', 'Change', 'thru1995']
	for i in range(1996, 2017):
		FOI_TEXT_LIST.append(str(i))

	trunk = int(len(FOI_TEXT_LIST)/thread_num) + 1
	p = Pool(thread_num)
	p.map(assign, range(thread_num))

	df = pd.read_csv(os.path.join(cwd, 'foitext_implant.txt'), sep='|', header=0, encoding='ISO-8859-1')
	print(df.shape[0])