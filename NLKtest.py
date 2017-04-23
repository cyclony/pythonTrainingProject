import nltk
from nltk.book import *
#text1.concordance("monstrous")

def get_sorted_dict(fdist):
    return sorted(fdist.items(), key=lambda d:d[1], reverse = True)

fdist1 = FreqDist(text1)  #调用ntlk的内部函数，实现统计词频
sortedDict = sorted(fdist1.items(), key=lambda d:d[1], reverse = True)
l = [ x[0] for x in sortedDict]
long_words = [x for x in l if len(x)>5 and fdist1[x]>200] #筛选长度大于5，并且词频多余200次的词
print(long_words[:50])

fdist4 = FreqDist(text4)
foursize_dict4 = get_sorted_dict(fdist4)
foursize_words = [x[0] for x in foursize_dict4[:10] if len(x[0]) == 3]
print(foursize_words)

