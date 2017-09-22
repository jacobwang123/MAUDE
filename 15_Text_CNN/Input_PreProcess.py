import numpy as np
import re
import itertools
from collections import Counter
from numpy import array
from numpy import argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    #No stopwords and stemming/lemmatizing
    # string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    # string = re.sub(r"\'s", " \'s", string)
    # string = re.sub(r"\'ve", " \'ve", string)
    # string = re.sub(r"n\'t", " n\'t", string)
    # string = re.sub(r"\'re", " \'re", string)
    # string = re.sub(r"\'d", " \'d", string)
    # string = re.sub(r"\'ll", " \'ll", string)
    # string = re.sub(r",", " , ", string)
    # string = re.sub(r"!", " ! ", string)
    # string = re.sub(r"\(", " \( ", string)
    # string = re.sub(r"\)", " \) ", string)
    # string = re.sub(r"\?", " \? ", string)
    # string = re.sub(r"\s{2,}", " ", string)

    # Stopwords and stemming/lemmatizing
    stop_words = stopwords.words('english')
    lmtzr = WordNetLemmatizer()
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = string.replace('"', ' ')
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " ", string)
    string = re.sub(r"!", " ", string)
    string = re.sub(r"\(", " ", string)
    string = re.sub(r"\)", " ", string)
    string = re.sub(r"\?", " ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = string.strip().lower()
    string = string.split(' ')
    l = len(string)
    for j in range(l):
	    i = l - 1 - j
	    string[i] = lmtzr.lemmatize(string[i])
	    if string[i] in stop_words:
		    string.pop(i)
    string = str(string)
    string = string.replace('[', '')
    string = string.replace(']', '')
    string = string.replace(',', '')
    string = string.replace("'", '')
    return string.strip().lower()


def load_data_and_labels(data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    text = []
    labels = []
    with open (data_file, 'r') as rf:
        n = 0
        for line in rf:
            n = n + 1
            line = line.replace('\n', '')
            line = line.split('|')
            text.append(str(line[0]))
            labels.append(int(line[1]))
        rf.close()
    print("Preprocessing data...")

    #One hot encoding for labels
    examples = [s.strip() for s in text]
    # Split by words
    x_text = [clean_str(sent) for sent in examples]
    # Generate labels
    labels = array(labels)
    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = labels.reshape(len(labels), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return [x_text, onehot_encoded]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]

#
# datafile = 'D:/Workplace/cnn-text-classification-tf/input.txt'
# a = load_data_and_labels(datafile)
# print(a)