#coding:utf-8
from sklearn import svm
from input_process import list_to_tfidf
from input_process import get_label
import numpy as np

str = input()
X,_,new_string = list_to_tfidf(str)
Y,_ = get_label()
clf = svm.SVC(C = 100, kernel = 'linear').fit(X,Y)
print(clf.predict(new_string))