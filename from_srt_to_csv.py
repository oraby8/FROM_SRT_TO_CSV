#This script converts .srt subtitle files to .csv files

from nltk.corpus import stopwords
import collections
from nltk.stem.porter import PorterStemmer
import string
import pandas as pd
counts = dict()



filepath='D:\\Friends\\Friends.S01E24.DVDrip.XviD-SAiNTS.srt'#srt file





def words_separator(filepath):
    file=open(filepath,'r')
    stetment=file.read()
    word=[word for word in stetment if word not in string.punctuation]
    word=[dig for dig in word if dig not in '1234567890']
    word=''.join(word)
    ##print(len(word))
    ps=PorterStemmer()

    word=[ps.stem(i) for i in word.split() if i.lower() not in stopwords.words('english')]
    return word
    ##print(len(word))

def words_counter(words):
    

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

word=words_separator(filepath)
dic=words_counter(word)
dic=collections.Counter(dic)

data=pd.DataFrame(list(dic.items()), columns=['word', 'count'])
data.to_csv('out.csv')


