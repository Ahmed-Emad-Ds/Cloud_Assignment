file = open('random_paragraphs.txt', 'r')
paragraph = file.read()
file.close()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

stop_words = stopwords.words('english')
paragraph_tokens = word_tokenize(paragraph)


paragraph_without_stopWords = []
for word in paragraph_tokens:
    if word.lower() not in stop_words:
        paragraph_without_stopWords.append(word)

freq = Counter(paragraph_without_stopWords)
for word, count in freq.items():
    print(word, ':', count)