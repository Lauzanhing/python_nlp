#coding:utf-8
import time
class segment:
    def __init__(self,sentence,maxlength):
        self.sentence = sentence
        self.maxlength = maxlength

    # 打开文件  把它放到一个list里面
    def file_fun():
        filename = 'C:\\Users\\Lauzanhing\\Desktop\\MYCODE\\pycode\\python_class\\chineseDic.txt'
        with open(filename,encoding='utf-8') as f:
            word_set = []
            word = f.readline().strip().split(',')
            count = 1
            while count <= 60366:
                word_set.append(word[0])
                word = f.readline().split(',')
                count = count + 1
        return word_set


    #正向最大匹配算法
    def forward_maxmatching(self):
        begin = 0
        end = self.maxlength
        max = self.maxlength
        sen = self.sentence
        word_set = segment.file_fun()
        words = []
        while begin < len(sen):
            if sen[begin:end] in word_set or end == begin + 1:
                words.append(sen[begin:end])
                begin = end
                end = end + max
            else:
                end = end - 1
        return words

    #逆向最大匹配算法
    def backward_maxmatching(self):
        begin = len(self.sentence) - self.maxlength
        end = len(self.sentence)
        max = self.maxlength
        sen = self.sentence
        word_set = segment.file_fun()
        words = []
        while begin > (0-max):
            if sen[begin:end] in word_set or begin == end - 1:
                words.append(sen[begin:end])
                end = begin
                begin = end - max
            else:
                begin = begin + 1
        words = list(reversed(words))
        return words


if __name__ == '__main__':
    sentence = input('请输入句子:')
    maxlength = input("请输入最大长度:")
    maxlength = int(maxlength)

    print("--------------------------------------------")

    # 正向匹配
    start = time.clock()

    正向匹配 = segment(sentence,maxlength)
    print("正向匹配结果：")
    正向结果 = '\\'.join(正向匹配.forward_maxmatching())
    print(正向结果)

    end = time.clock()
    print('分词时间: %s Seconds' % (end - start))

    print("--------------------------------------------")

    # 逆向匹配
    start = time.clock()

    逆向匹配 = segment(sentence,maxlength)
    print("逆向匹配结果")
    逆向结果 = '\\'.join(逆向匹配.forward_maxmatching())
    print(逆向结果)

    end = time.clock()
    print('分词时间: %s Seconds' % (end - start))

    print("--------------------------------------------")