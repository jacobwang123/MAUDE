# website for wordcloud: http://www.wordclouds.com/
import math
with open('Word_Cloud.txt', 'r') as rf:
	with open('Word_Cloud_Optimized_Text.txt', 'w') as wf:
		m = 0
		for line in rf:
			line = line.replace('\n', '')
			line = line.split('\t')
			line[0] = int(math.log(int(line[0]), 2))
			if line[0] >= 5:
				wf.write(str(line[0] * 4) + '\t' + str(line[1] + '\n'))
		wf.close()
	rf.close()
