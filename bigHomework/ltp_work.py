#coding:utf-8
"""
1.先处理文本
2.去除停用词
3.分词
4.词性标注
5.命名实体识别
6.词频统计

"""
import json
import os
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import SentenceSplitter
from pyltp import NamedEntityRecognizer
# 处理文本
def process_raw():
    with open("data/dream_of_red_chamber.txt",'r+',encoding='utf-8') as f:
        contents = f.read()
        new_contents = contents.replace('\n','').replace('\t','').replace('　　','')
        with open('data/raw_test.txt','r+',encoding='utf-8') as w:
            w.write(new_contents)
        w.close()
    f.close()

# 去除停用词
def stopword():
    with open('data/stopwords.txt','r') as f:
        with open('data/seg.txt','r') as w:
            word = f.readline()
            contents = w.read()
            while word:
                word = word.replace('\n','')
                contents = contents.replace(word,'')
                word = f.readline()
            with open('data/After_stopword.txt','w') as r:
                r.write(contents)

def segsent():
    with open('data/raw_test.txt','r') as f:
        contents = f.read()
    sents = SentenceSplitter.split(contents)
    # print '\n'.join(sents)
    content = '\n'.join(sents)
    # print(content)
    with open('data/After_stopword.txt','w') as w:
        w.write(content)

def segword():
    LTP_DATA_DIR = 'ltp_data_v3.4.0'  # ltp模型目录的路径
    cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

    segmentor = Segmentor()  # 初始化实例
    segmentor.load_with_lexicon(cws_model_path, 'data/names.txt')  # 加载模型，第二个参数是您的外部词典文件路径
    with open('data/After_stopword.txt','r') as f:
        with open('data/seg.txt','w') as w:
            content = f.readline()
            while content:
                words = segmentor.segment(content)
                words = '\t'.join(words)
                w.write(words)
                w.write('\n')
                content = f.readline()
    # print '\t'.join(words)
    segmentor.release()

def pos():
    LTP_DATA_DIR = 'ltp_data_v3.4.0'  # ltp模型目录的路径
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

    postagger = Postagger()  # 初始化实例
    postagger.load(pos_model_path)  # 加载模型

    with open('data/seg.txt','r') as f:
        with open('data/pos.txt','w') as w:
            contents = f.readline()
            while contents:
                contents = contents.split('\t')
                postags = postagger.postag(contents)
                w.write('\t'.join(postags))
                w.write('\n')
                contents = f.readline()
    postagger.release()  # 释放模型

def ner():
    LTP_DATA_DIR = 'ltp_data_v3.4.0'  # ltp模型目录的路径
    ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')


    recognizer = NamedEntityRecognizer()  # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型

    with open('data/seg.txt','r') as seg:
        with open('data/pos.txt','r') as pos:
            with open('data/ner.txt','w') as ner:
                segword = seg.readline()
                posword = pos.readline()
                while segword:
                    seg_list = segword.split('\t')
                    pos_list = posword.split('\t')
                    netags = recognizer.recognize(seg_list,pos_list)
                    netags = '\t'.join(netags)
                    ner.write(netags)
                    ner.write('\n')
                    segword = seg.readline()
                    posword = pos.readline()

    recognizer.release()  # 释放模型

def count_per_sent_name_verb():
    with open('data/seg.txt','r') as seg, open('data/pos.txt','r') as pos,\
            open('data/ner.txt','r') as ner,open('data/count.txt','w') as w\
            ,open('data/stopwords.txt','r') as s:
        segword = seg.readline()
        posword = pos.readline()
        nerword = ner.readline()
        stopword = s.read()
        stopword_list = stopword.split('\n')
        name = []
        verb = []
        while segword:
            seg_list = segword.split('\t')
            pos_list = posword.split('\t')
            ner_list = nerword.split('\t')
            if('S-Nh' in ner_list):
                for i in range(0,len(ner_list)):
                    if(ner_list[i] == 'S-Nh'):
                        name.append(seg_list[i])
                for i in range(0,len(seg_list)):
                    if(pos_list[i] == 'v'):
                        if(seg_list[i] not in stopword_list):
                            verb.append(seg_list[i])
            segword = seg.readline()
            posword = pos.readline()
            nerword = ner.readline()
    seg.close()
    with open('data/seg.txt','r') as seg:
        name = set(name)
        verb = set(verb)
        name_dict = {}
        verb_dict = {}
        for item in name:
            name_dict[item] = 1
        for item in verb:
            verb_dict[item] = 1
        segword = seg.readline()
        while segword:
        #     seg_list = segword.split('\t')
        #     for word in seg_list:
        #         for item in name:
        #             if(word == item):
        #                 name_dict[item] += 1
        #     segword = seg.readline()
        # name_list = sorted(name_dict.items(), key=lambda x: x[1], reverse=True)
        # print(name_list[:50])
            seg_list = segword.split('\t')
            for word in seg_list:
                for item in verb:
                    if (word == item):
                        verb_dict[item] += 1
            segword = seg.readline()
        verb_list = sorted(verb_dict.items(), key=lambda x: x[1], reverse=True)
        b = verb_list[:150]
        result = json.dumps(b, encoding='UTF-8', ensure_ascii=False)
        print(result)

count_per_sent_name_verb()