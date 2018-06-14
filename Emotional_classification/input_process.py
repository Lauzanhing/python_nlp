#coding:utf-8
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
# corpus = ['This is the first document.',
#           'This is the second second document.']
#
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(corpus)
# # print(X.toarray())
# counts = X.toarray()
# transformer = TfidfTransformer(smooth_idf=True)
# tfidf = transformer.fit_transform(counts)
# print(tfidf.toarray())

def data_for_train():
    with open('data/amazon_cells_labelled.txt','r')as f,\
            open('data/train.txt','w') as w1,\
            open('data/test.txt','w') as w2:
        data_list = []
        count = 0
        line = f.readline()
        while count < 800:
            line = ''.join(line)
            # print(line[:-2])
            # print(line[-2:-1])
            w1.write(line)
            line = f.readline()
            count = count + 1
        while 800 <= count < 1000:
            line = ''.join(line)
            # print(line[:-2])
            w2.write(line)
            line = f.readline()
            count = count + 1

def data_to_list(new_string):
    with open('data/train.txt','r') as r1,\
         open('data/test.txt','r') as r2:
        raw_list = []
        train_line = r1.readline()
        test_line = r2.readline()
        while train_line:
            train_line = ''.join(train_line)
            raw_list.append(train_line[:-3])
            train_line = r1.readline()
        while test_line:
            test_line = ''.join(test_line)
            raw_list.append(test_line[:-3])
            test_line = r2.readline()
        raw_list.append(new_string)
        return raw_list
# data_to_list("111")
def list_to_tfidf(new_string):
    vectorizer = CountVectorizer()
    raw_list = data_to_list(new_string)
    One_hot = vectorizer.fit_transform(raw_list)
    # print(One_hot.toarray().shape)
    counts = One_hot.toarray()
    transformer = TfidfTransformer(smooth_idf=True)
    tfidf = transformer.fit_transform(counts)
    train_tfidf = np.array(tfidf.toarray()[:800])
    test_tfidf = np.array(tfidf.toarray()[800:1000])
    new_tfidf = np.array(tfidf.toarray()[1000:1001])
    return  train_tfidf,test_tfidf,new_tfidf
# list_to_tfidf("111")
def get_label():
    with open('data/train.txt', 'r') as r1, \
            open('data/test.txt', 'r') as r2:
        label_list = []
        train_line = r1.readline()
        test_line = r2.readline()
        while train_line:
            train_line = ''.join(train_line)
            label_list.append(train_line[-2:-1])
            train_line = r1.readline()
        while test_line:
            test_line = ''.join(test_line)
            label_list.append(test_line[-2:-1])
            test_line = r2.readline()
        label_list = np.array(label_list)
        train_label = label_list[:800]
        test_label = label_list[800:1000]
    return train_label,test_label
# get_label()