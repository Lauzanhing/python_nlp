import re
import nltk
# a
text = 'some text with long-\nterm and encyclo-\npedia'
words = re.findall(r'\w+\-\n\w+', text)
print(words)


#b
for w in words:
    print(re.sub('\n','',w))

#c
for w in words:
    word = re.sub('\n','',w)
    parts = word.lower().split('-')
    if(parts[0] not in nltk.corpus.words.words() and parts[1] not in nltk.corpus.words.words()):
        print(re.sub('\-','',word))
    else:
        print(word)