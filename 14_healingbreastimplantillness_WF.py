import os
import re
from collections import Counter
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
import requests
from bs4 import BeautifulSoup

cwd = os.path.dirname(os.path.realpath(__file__))

url = 'http://healingbreastimplantillness.com/breast-implant-symptoms/'

lmtzr = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
stopwords = nltk.corpus.stopwords.words('english')

def processLine(line):
	line = re.sub(r'https?:\/\/.*\s+', ' ', line, flags=re.MULTILINE) # remove URLs
	line = re.sub(r'\W+',' ',line, flags=re.MULTILINE) # remove non-word characters
	
	line = line.lower()
	tokens = tokenizer.tokenize(line)
	output = []
	for t in tokens:
		t = lmtzr.lemmatize(t)
		if (len(t) <= 2) or (len(t) >= 8) or (t in stopwords) or (t.isdigit()):
			continue
		output.append(t)
	return ' '.join(output)

if __name__ == '__main__':
	response = requests.get(url).text
	soup = BeautifulSoup(response, "lxml")
	comments = soup.find_all('section', class_="comment-content comment")
	full_text = ''
	for c in comments:
		processed = processLine(c.text)
		full_text += processed

	full_text = full_text.split(' ')
	counts = Counter(full_text)
	with open(os.path.join(cwd, 'website_WF.txt'), 'w') as f:
		for k, v in counts.most_common():
			f.write( "{}\t{}\n".format(v, k))