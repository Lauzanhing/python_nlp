import nltk
from nltk.corpus import gutenberg as gb

# print(nltk.corpus.gutenberg.fileids())

# emma = nltk.corpus.gutenberg.words("austen-emma.txt")
# print(emma)

# for fileid in gb.fileids():
#     num_chars = len(gb.raw(fileid))
#     num_words = len(gb.words(fileid))
#     num_sents = len(gb.sents(fileid))
#     num_vocab = len(set([w.lower() for w in gb.words(fileid)]))
#     print(int(num_chars/num_words),int(num_words/num_sents),int(num_words/num_vocab),fileid)

# from nltk.corpus import webtext
# for fileid in webtext.fileids():
#     print(fileid,webtext.raw(fileid)[:65])

# from nltk.corpus import nps_chat
# chatroom = nps_chat.posts('10-19-20s_706posts.xml')
# print(chatroom[123])

from nltk.corpus import brown
print(brown.categories())
print(brown.words(categories = 'news'))
print(brown.words(fileids=['cg22']))
