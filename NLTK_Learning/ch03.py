from nltk.corpus import gutenberg as gb
import re
# emma = gb.words('austen-emma.txt')
# word = [w for w in emma if re.search(r'sh',w) and len(w) >= 4]
# print(word)

# cards = ['1234 5678 1234 5678','12 5678 1234 5678','1234 5678 1234 5678,','1234 5678 1234 5678-']
# word = [w for w in cards if re.search('([0-9]{4}\s){3}([0-9]{4}$ )',w)]
# print(word)


words = "we are doing some thing [vp3,2-]. What age [fm1,s-] the industry"
word = re.findall('.*?(\[.*?]).*?',words)
print(word)