__author__ = 'Soumik'
import nltk, re, pprint
from nltk import word_tokenize as wt
import codecs
f=open("pos.wn")
raw=f.read()
tokens=wt(raw)
text=nltk.Text(tokens)
g=[]
for x in tokens:
    y=x.replace("_"," ")
    g.append(y)
print(g)
f1=open("neg.wn")
raw1=f1.read()
tokens1=wt(raw1)
text1=nltk.Text(tokens1)
h=[]
for z in tokens1:
    a=z.replace("_"," ")
    h.append(a)
print("\n",h)

pcount=0
ncount=0

for x in h:
    if x in open("posTweets.txt", encoding="utf8").read():
        pcount=pcount+1
print("The number of positive tweets are:%s",pcount)

for x in h:
    if x in open("negTweets.txt", encoding="utf8").read():
        ncount=ncount+1

print("The number of negative tweets are:",ncount)

pintweet=0
nintweet=0


with codecs.open('posTweets.txt','r',encoding='utf-8') as f:
    for line in f.readlines():
        for x in g:
            if x in line:
                pintweet=pintweet+1
        words = len(line.strip(' '))
        print(words)
with codecs.open('negTweets.txt','r',encoding='utf-8') as f1:
    for line1 in f1.readlines():
        for y in h:
            if y in line1:
                nintweet=nintweet+1
        words1= len(line1.strip(' '))
        print(words1)

print("the number of n words in ntweet is:", nintweet)
print("the number of p words in ptweet is:", pintweet)