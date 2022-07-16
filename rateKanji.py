import math
import numpy as np

def rating_func(index):
    return 1 - math.sinh(index/6000 * math.asinh(1))

def get_kanji(filename_kanjiList):
    with open(filename_kanjiList, 'r', encoding='utf-8') as file:
        kanji = file.read()
    
    kanji = kanji.split(" ")
    return kanji
    
def get_words(filename_wordList):
    with open(filename_wordList, 'r', encoding='utf-8') as file:
        words = file.read()

    words = words.split(" ")
    return words

def get_rating(character, words):
    rating = 0
    for i in range(len(words)):
        if character in words[i]:
            rating += rating_func(i)
    
    return rating
    
filename_kanjiList = "kanji_list.txt"
filename_wordList = "word_list.txt"

kanji = get_kanji(filename_kanjiList)
words = get_words(filename_wordList)

kanji_rating = np.zeros(len(kanji))
for i in range(len(kanji)):
    kanji_rating[i] = get_rating(kanji[i], words)
    
idx = np.argsort(-kanji_rating)    
kanji_rating = kanji_rating[idx]/kanji_rating.max()
kanji = np.asarray(kanji)[idx]

with open("kanji_ratings.txt", 'w', encoding = 'utf-8') as file:
    for i in range(len(kanji)):
        file.write(f"{kanji[i]} {kanji_rating[i]:.5f}\n")



