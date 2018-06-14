#coding:utf-8
from collections import Counter
from math import log, pow, sqrt

def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA ** 0.5) * (normB ** 0.5)) * 100, 2)


def cosine(vec1, vec2):
    return cosine_similarity(vec1, vec2)

def prepro():
    doc1 = "Glimpse is an indexing and query system that allows for search through a file system or document collection " \
           "quickly. Glimpse is the default search engine in a larger information retrieval system. It has also been used " \
           "as part of some web based search engines. "
    doc2 = "The main processes in an retrieval system are document indexing, query processing, query evaluation and " \
           "relevance feedback. Among these, efficient updating of the index is critical in large scale systems. "
    doc3 = "Clusters are created from short snippets of documents retrieved by web search engines which are as good as " \
           "clusters created from the full text of web documents. "
    doc = [doc1, doc2, doc3]

    stop_words = "a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can," \
                 "cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his," \
                 "how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor," \
                 "not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the," \
                 "their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while," \
                 "who,whom,why,will,with,would,yet,you,your,., "
    stop_words = [w for w in stop_words.split(",")]

    # segment
    # 分词，去停用词与标点
    all_words = [w.replace(",", "").replace(".", "") for w in str(doc1 + doc2 + doc3).split(" ") if w not in stop_words]
    # 去重
    all_words = list(set(all_words))
    all_words = sorted(all_words)
    return doc, all_words


def get_idf(word):
    string = word + "#"  # for task 1
    sum = 0
    pos=0
    for i in range(len(doc)):

        d = doc[i]
        if word in d:
            sum += 1
            string += str(i + 1) if pos == 0 else ("~" + str(i + 1))
            pos+=1
    result = log(len(doc) / sum)
    if sum == 0:
        result = 0
    string = string.split("#")
    string = string[0] + "#" + str(sum) + "#" + string[1]
    # print(string)
    return  result


def weight(t, idf):
    return log(1 + t) * idf


def doc2vec(Doc):
# convert document to vector
#将文档转化成向量
    list = []
    for w in all_words:
        c = Counter(Doc.split(" "))
        t = c[w]
        idf = get_idf(word=w)
        w_weight = weight(t=t, idf=idf)
        list.append(w_weight)
    return list




if __name__ == '__main__':
    doc, all_words = prepro()
    doc1, doc2, doc3 = doc[0], doc[1], doc[2]
    query = "search engine index"

    print("query vector:", doc2vec(query))
    print()
    for i in range(len(doc)):
        d = doc[i]
        print("doc" + str(i) + " vector:", doc2vec(d))
        print("similarity:", cosine(doc2vec(query), doc2vec(d)))
