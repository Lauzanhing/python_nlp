#coding:utf-8

from sklearn import metrics
from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
from sklearn import tree
from sklearn import svm
from input_process import list_to_tfidf
from input_process import get_label

train_tfidf,test_tfidf,_ = list_to_tfidf("")
train_label,test_label = get_label()
X = train_tfidf
Y = train_label
X_test = test_tfidf
Y_test = test_label

"""
高斯多项式结果：
             precision    recall  f1-score   support

          0       0.73      0.61      0.67       109
          1       0.61      0.73      0.66        91

avg / total       0.67      0.67      0.67       200
"""
def GaussianNB_model():
    clf = GaussianNB().fit(X,Y)
    joblib.dump(clf, 'model/GaussianNB_model.pkl')
    print("高斯多项式结果：")
    print(metrics.classification_report(Y_test, clf.predict(X_test)))
GaussianNB_model()

"""
多项式贝叶斯结果：
             precision    recall  f1-score   support

          0       0.89      0.73      0.80       109
          1       0.74      0.89      0.81        91

avg / total       0.82      0.81      0.80       200
"""
def MultinomialNB_model():
    clf = MultinomialNB().fit(X,Y)
    joblib.dump(clf, 'model/MultinomialNB_model.pkl')
    print("多项式贝叶斯结果：")
    print(metrics.classification_report(Y_test, clf.predict(X_test)))
MultinomialNB_model()

"""
伯努利贝叶斯结果:
             precision    recall  f1-score   support

          0       0.82      0.70      0.75       109
          1       0.69      0.81      0.75        91

avg / total       0.76      0.75      0.75       200
"""
def BernoulliNB_model():
    clf = BernoulliNB().fit(X, Y)
    joblib.dump(clf, 'model/BernoulliNB_model.pkl')
    print("伯努利贝叶斯结果:")
    print(metrics.classification_report(Y_test, clf.predict(X_test)))
BernoulliNB_model()

"""
决策树结果：
             precision    recall  f1-score   support

          0       0.73      0.79      0.76       109
          1       0.72      0.65      0.68        91

avg / total       0.72      0.72      0.72       200
"""
def DStree_model():
    clf = tree.DecisionTreeClassifier().fit(X,Y)
    joblib.dump(clf, 'model/DStree_model.pkl')
    print("决策树结果：")
    print(metrics.classification_report(Y_test, clf.predict(X_test)))
DStree_model()

"""
支撑向量机结果：
             precision    recall  f1-score   support

          0       0.82      0.87      0.84       109
          1       0.83      0.77      0.80        91

avg / total       0.83      0.82      0.82       200
"""
def svm_model():
    clf = svm.SVC(C = 100, kernel = 'linear').fit(X,Y)
    joblib.dump(clf, 'model/svm_model.pkl')
    print("支撑向量机结果：")
    print(metrics.classification_report(Y_test, clf.predict(X_test)))
svm_model()