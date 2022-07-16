import numpy as np
import matplotlib
import matplotlib.pyplot as py

import rateKanji as rK

matplotlib.rcParams["figure.dpi"] = 300

filename_kanjiList = "kanji_list.txt"
filename_wordList = "word_list.txt"

kanji = rK.get_kanji(filename_kanjiList)
words = rK.get_words(filename_wordList)

kanji_rating = np.zeros(len(kanji))
for i in range(len(kanji)):
    kanji_rating[i] = rK.get_rating(kanji[i], words)
    
idx = np.argsort(-kanji_rating)    
kanji_rating = kanji_rating[idx]/kanji_rating.max()
kanji = np.asarray(kanji)[idx]

with py.style.context("bmh"):
    py.rcParams['axes.facecolor'] = 'none'
    py.plot(kanji_rating)  
    #py.bar(np.arange(1,len(kanji_rating) + 1) - 0.4,kanji_rating[:])
    py.show()